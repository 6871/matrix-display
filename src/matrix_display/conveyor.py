#!/usr/bin/env python3
"""Module defining Conveyor class.
"""
from matrix_display.canvas import Canvas
import matrix_display.rgb_colours as rgb_colours
import time


class Conveyor:
    """Prints rows of data on a matrix display, scrolling long rows. Row data
    may be static or sourced from a function that gets periodically
    re-evaluated.
    """
    def __init__(self, display, scroll_delay=0.03):
        """Initialise the display with an external display driver object.

        Parameters
        ----------
        display : matrix_display.Display
            External display driver that extends matrix_display.Display
        scroll_delay : float
            Time in seconds to wait between each refresh of the display.
        """
        self.display = display
        self.scroll_delay = scroll_delay
        self.width = display.col_count
        self.height = display.row_count
        self.sources = []
        self.capacity = self.height

    def add_row(self, content, reload_wait_time=15, *args, **kwargs):
        """Adds a row of content to the display.

        Parameters
        ----------
        content : str or bytes or tuple or function or list or Canvas
            The row's content
        reload_wait_time : float
            Time to wait before refreshing dynamic content from a function
        *args
            Optional list of arguments to pass to content function
        **kwargs
            Optional list of keyword arguments to pass to content function

        Returns
        -------
        status : boolean
            True if display has room for the content and it was added OK.
        """
        source = self.DisplaySource(
            content, self.width, self.scroll_delay, reload_wait_time,
            *args, **kwargs)

        if source.canvas.height() <= self.capacity:
            self.sources.append(source)
            self.capacity -= source.canvas.height()
            return True
        else:
            return False

    def play(self):
        """Evaluates and displays content assigned with add_row."""
        while True:
            dy_ptr = 0  # display y axis pointer
            for source in self.sources:
                for row in source.canvas.rows:
                    for dx_ptr in range(self.width):
                        rgb = rgb_colours.black
                        canvas_pixel = dx_ptr + source.scroll_ptr
                        if canvas_pixel < source.canvas.width():
                            rgb = row[canvas_pixel]
                        self.display.set_pixel(
                            dy_ptr, dx_ptr, rgb[0], rgb[1], rgb[2])
                    dy_ptr += 1
                source.scroll_handler()  # Shift display left for long source

            self.display.draw()
            time.sleep(self.scroll_delay)

    class DisplaySource:
        """Represents a source of content for a row on the display."""
        def __init__(self, content, display_width, scroll_delay,
                     data_reload_wait_time, *args, **kwargs):
            """Initialise this display row, render its initial canvas content.

            Parameters
            ----------
            content : str or tuple or function or list
                A content item assigned to the display by add_row
            display_width : int
                The width of the display being used (required for scrolling)
            *args
                Optional list of arguments to pass to content function
            **kwargs
                Optional list of keyword arguments to pass to content function
            """
            self.initialised = False
            self.scroll_ptr = 0
            self.display_width = display_width
            self.content = content
            self.content_args = args
            self.content_kwargs = kwargs
            self.canvas = None
            self.scroll_delay = scroll_delay
            self.data_reload_wait_time = data_reload_wait_time
            self.data_reload_ttl = self.data_reload_wait_time
            self._redraw_canvas()
            self.initialised = True

        def scroll_handler(self):
            """Called on each display redraw so scrolling can be incremented
            and dynamic content can be reloaded."""
            reload_data = False
            self.data_reload_ttl -= self.scroll_delay
            if self.data_reload_ttl <= 0:
                reload_data = True

            if self.canvas.width() > self.display_width:  # scrolling required
                self.scroll_ptr += 1

                if self.scroll_ptr > self.canvas.width():
                    self.scroll_ptr = 0  # scrolled off screen, reset to start
                    if reload_data:
                        self._redraw_canvas()  # reload data while row blank
                        self.data_reload_ttl = self.data_reload_wait_time
            else:  # not scrolling, but dynamic content may need refresh
                if callable(self.content) and reload_data:
                    self._redraw_canvas()
                    self.data_reload_ttl = self.data_reload_wait_time

        def _add_scroll_lpad(self):
            """Internal method used to make scrolled content roll in."""
            if self.canvas.width() > self.display_width:
                self.canvas = Canvas(
                    lpad_count=self.display_width,
                    row_count=self.canvas.height()
                ).append_canvas(self.canvas)

        def _redraw_canvas(self):
            """Internal method to draw display row's canvas."""
            if self.initialised:  # keep existing height in case of more rows
                self.canvas = Canvas(row_count=self.canvas.height())
            else:  # initial content sets the canvas height
                # if isinstance(self.content, Canvas):
                #     self.canvas = Canvas(row_count=self.content.height())
                # else:
                #     self.canvas = Canvas()
                self.canvas = Canvas(row_count=0)

            self._process_content(self.content)
            self._add_scroll_lpad()

        def _process_content(self, value):
            """Internal method to normalise list and function content."""
            if type(value) is list:
                for list_item in value:
                    self._process_content(list_item)
            elif callable(value):
                self._process_content(
                    value(*self.content_args, **self.content_kwargs))
            else:
                self._append_content(value)

        def _append_content(self, value):
            """Internal method to append normalised content to canvas."""
            if not self.initialised and len(self.canvas.rows) == 0:
                # Size canvas on first use according to content type
                if isinstance(value, Canvas):
                    self.canvas.add_rows(value.height())
                else:
                    self.canvas.add_rows(len(self.canvas.charset['0']))

            if type(value) is str:
                self.canvas.append_text(value)
            elif type(value) is tuple:
                self.canvas.append_text(value[0], value[1])
            elif isinstance(value, Canvas):
                if value.height() > self.canvas.height():
                    if self.initialised:
                        # canvas already assigned to display, truncate to fit
                        value.delete_rows(
                            value.height() - self.canvas.height())
                self.canvas.append_canvas(value)
            else:
                raise ValueError((
                    f"Can't append content type \"{type(value)}\" (with "
                    f"value \"{value}\"); require str, tuple or Canvas "
                    f"(id(Canvas)=\"{id(Canvas)}\", "
                    f"id(value.__class__)=\"{id(value.__class__)}\")"))
