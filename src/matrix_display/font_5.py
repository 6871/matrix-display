#!/usr/bin/env python3
"""Module to map an individual character string to a 5-row pixel-based matrix
representation that can be rendered on an LED display; use the "lookup"
dictionary object to return the matrix representation of a single character.

Examples
--------
>>> from matrix_display import font_5
>>> font_5.lookup['.']
[[0], [0], [0], [0], [1]]
>>> font_5.lookup['L']
[[1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 1, 1]]
>>>
"""
chr_0 = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 0, 1],
    [1, 0, 1],
    [1, 1, 1]
]

chr_1 = [
    [1],
    [1],
    [1],
    [1],
    [1]
]

chr_2 = [
    [1, 1, 1],
    [0, 0, 1],
    [1, 1, 1],
    [1, 0, 0],
    [1, 1, 1]
]

chr_3 = [
    [1, 1, 1],
    [0, 0, 1],
    [1, 1, 1],
    [0, 0, 1],
    [1, 1, 1]
]

chr_4 = [
    [1, 0, 1],
    [1, 0, 1],
    [1, 1, 1],
    [0, 0, 1],
    [0, 0, 1]
]

chr_5 = [
    [1, 1, 1],
    [1, 0, 0],
    [1, 1, 1],
    [0, 0, 1],
    [1, 1, 1]
]

chr_6 = [
    [1, 1, 1],
    [1, 0, 0],
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

chr_7 = [
    [1, 1, 1],
    [0, 0, 1],
    [0, 0, 1],
    [0, 0, 1],
    [0, 0, 1]
]

chr_8 = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

chr_9 = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1],
    [0, 0, 1],
    [1, 1, 1]
]

chr_a = [
    [1, 1, 0],
    [0, 0, 1],
    [0, 1, 1],
    [1, 0, 1],
    [0, 1, 1]
]

chr_b = [
    [1, 0, 0],
    [1, 0, 0],
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

chr_c = [
    [0, 0, 0],
    [0, 0, 0],
    [1, 1, 1],
    [1, 0, 0],
    [1, 1, 1]
]

chr_d = [
    [0, 0, 1],
    [0, 0, 1],
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

chr_e = [
    [0, 1, 0],
    [1, 0, 1],
    [1, 1, 1],
    [1, 0, 0],
    [0, 1, 1]
]

chr_f = [
    [0, 1, 1],
    [0, 1, 0],
    [1, 1, 1],
    [0, 1, 0],
    [0, 1, 0]
]

chr_g = [
    [0, 1, 1],
    [1, 0, 1],
    [0, 1, 1],
    [0, 0, 1],
    [1, 1, 0]
]

chr_h = [
    [1, 0, 0],
    [1, 0, 0],
    [1, 1, 1],
    [1, 0, 1],
    [1, 0, 1]
]

chr_i = [
    [0],
    [1],
    [0],
    [1],
    [1]
]

chr_j = [
    [0, 0, 1],
    [0, 0, 0],
    [0, 0, 1],
    [1, 0, 1],
    [0, 1, 0]
]

chr_k = [
    [1, 0, 0],
    [1, 0, 1],
    [1, 1, 0],
    [1, 1, 0],
    [1, 0, 1]
]

chr_l = [
    [1, 0],
    [1, 0],
    [1, 0],
    [1, 0],
    [0, 1]
]

chr_m = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1]
]

chr_n = [
    [0, 0, 0],
    [0, 0, 0],
    [1, 1, 0],
    [1, 0, 1],
    [1, 0, 1]
]

chr_o = [
    [0, 0, 0],
    [0, 1, 0],
    [1, 0, 1],
    [1, 0, 1],
    [0, 1, 0]
]

chr_p = [
    [0, 0, 0],
    [1, 1, 0],
    [1, 0, 1],
    [1, 1, 0],
    [1, 0, 0]
]

chr_q = [
    [0, 1, 1],
    [1, 0, 1],
    [0, 1, 1],
    [0, 0, 1],
    [0, 0, 1]
]

chr_r = [
    [0, 0, 0],
    [0, 0, 0],
    [1, 1, 1],
    [1, 0, 0],
    [1, 0, 0]
]

chr_s = [
    [0, 1, 1],
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 0]
]

chr_t = [
    [0, 1, 0],
    [1, 1, 1],
    [0, 1, 0],
    [0, 1, 0],
    [0, 0, 1]
]

chr_u = [
    [0, 0, 0],
    [0, 0, 0],
    [1, 0, 1],
    [1, 0, 1],
    [0, 1, 1]
]

chr_v = [
    [0, 0, 0],
    [0, 0, 0],
    [1, 0, 1],
    [1, 0, 1],
    [0, 1, 0]
]

chr_w = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0]
]

chr_x = [
    [0, 0, 0],
    [0, 0, 0],
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 1]
]

chr_y = [
    [1, 0, 1],
    [1, 0, 1],
    [0, 1, 1],
    [0, 0, 1],
    [1, 1, 0]
]

chr_z = [
    [0, 0, 0, 0],
    [1, 1, 1, 1],
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 1, 1]
]

chr_a_up = [
    [0, 1, 0],
    [1, 0, 1],
    [1, 1, 1],
    [1, 0, 1],
    [1, 0, 1]
]

chr_b_up = [
    [1, 1, 0],
    [1, 0, 1],
    [1, 1, 0],
    [1, 0, 1],
    [1, 1, 0]
]

chr_c_up = [
    [0, 1, 1],
    [1, 0, 0],
    [1, 0, 0],
    [1, 0, 0],
    [0, 1, 1]
]

chr_d_up = [
    [1, 1, 0],
    [1, 0, 1],
    [1, 0, 1],
    [1, 0, 1],
    [1, 1, 0]
]

chr_e_up = [
    [1, 1, 1],
    [1, 0, 0],
    [1, 1, 0],
    [1, 0, 0],
    [1, 1, 1]
]

chr_f_up = [
    [1, 1, 1],
    [1, 0, 0],
    [1, 1, 0],
    [1, 0, 0],
    [1, 0, 0]
]

chr_g_up = [
    [0, 1, 1, 1],
    [1, 0, 0, 0],
    [1, 0, 1, 1],
    [1, 0, 0, 1],
    [0, 1, 1, 0]
]

chr_h_up = [
    [1, 0, 1],
    [1, 0, 1],
    [1, 1, 1],
    [1, 0, 1],
    [1, 0, 1]
]

chr_i_up = [
    [1, 1, 1],
    [0, 1, 0],
    [0, 1, 0],
    [0, 1, 0],
    [1, 1, 1]
]

chr_j_up = [
    [1, 1, 1, 1],
    [0, 0, 1, 0],
    [0, 0, 1, 0],
    [1, 0, 1, 0],
    [0, 1, 0, 0]
]

chr_k_up = [
    [1, 0, 1],
    [1, 1, 0],
    [1, 0, 0],
    [1, 1, 0],
    [1, 0, 1]
]

chr_l_up = [
    [1, 0, 0],
    [1, 0, 0],
    [1, 0, 0],
    [1, 0, 0],
    [1, 1, 1]
]

chr_m_up = [
    [1, 0, 0, 0, 1],
    [1, 1, 0, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1]
]

chr_n_up = [
    [1, 0, 0, 0, 1],
    [1, 1, 0, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 0, 1, 1],
    [1, 0, 0, 0, 1]
]

chr_o_up = [
    [0, 1, 0],
    [1, 0, 1],
    [1, 0, 1],
    [1, 0, 1],
    [0, 1, 0]
]

chr_p_up = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1],
    [1, 0, 0],
    [1, 0, 0]
]

chr_q_up = [
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1]
]

chr_r_up = [
    [1, 1, 0],
    [1, 0, 1],
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1]
]

chr_s_up = [
    [1, 1, 1],
    [1, 0, 0],
    [1, 1, 1],
    [0, 0, 1],
    [1, 1, 1]
]

chr_t_up = [
    [1, 1, 1],
    [0, 1, 0],
    [0, 1, 0],
    [0, 1, 0],
    [0, 1, 0]
]

chr_u_up = [
    [1, 0, 1],
    [1, 0, 1],
    [1, 0, 1],
    [1, 0, 1],
    [1, 1, 1]
]

chr_v_up = [
    [1, 0, 1],
    [1, 0, 1],
    [1, 0, 1],
    [1, 0, 1],
    [0, 1, 0]
]

chr_w_up = [
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0]
]

chr_x_up = [
    [1, 0, 1],
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 1],
    [1, 0, 1]
]

chr_y_up = [
    [1, 0, 1],
    [1, 0, 1],
    [1, 0, 1],
    [0, 1, 0],
    [0, 1, 0]
]

chr_z_up = [
    [1, 1, 1],
    [0, 0, 1],
    [0, 1, 0],
    [1, 0, 0],
    [1, 1, 1]
]

chr_dot = [
    [0],
    [0],
    [0],
    [0],
    [1]
]

chr_space = [
    [0],
    [0],
    [0],
    [0],
    [0]
]

chr_colon = [
    [0],
    [1],
    [0],
    [1],
    [0]
]

chr_equals = [
    [0, 0, 0],
    [1, 1, 1],
    [0, 0, 0],
    [1, 1, 1],
    [0, 0, 0]
]

chr_exclamation = [
    [1],
    [1],
    [1],
    [0],
    [1]
]

chr_comma = [
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 1],
    [1, 0]
]

chr_underscore = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [1, 1, 1]
]

chr_minus = [
    [0, 0, 0],
    [0, 0, 0],
    [1, 1, 1],
    [0, 0, 0],
    [0, 0, 0]
]

chr_plus = [
    [0, 0, 0],
    [0, 1, 0],
    [1, 1, 1],
    [0, 1, 0],
    [0, 0, 0]
]

chr_forward_slash = [
    [0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0]
]

chr_back_slash = [
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1]
]

chr_asterisk = [
    [0, 0, 1, 0, 0],
    [1, 0, 1, 0, 1],
    [0, 1, 1, 1, 0],
    [0, 1, 0, 1, 0],
    [1, 0, 0, 0, 1]
]

chr_at = [
    [0, 1, 1, 1, 0],
    [1, 0, 0, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 0, 1, 1],
    [0, 1, 0, 0, 0]
]

chr_single_quote = [
    [1],
    [1],
    [0],
    [0],
    [0]
]

chr_double_quote = [
    [1, 0, 1],
    [1, 0, 1],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

chr_gbp = [
    [0, 1, 1],
    [0, 1, 0],
    [1, 1, 1],
    [0, 1, 0],
    [1, 1, 1]
]

chr_usd = [
    [1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1]
]

chr_eur = [
    [0, 0, 1, 1],
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 1]
]

chr_percent = [
    [1, 0, 0, 0, 1],
    [1, 0, 0, 1, 0],
    [0, 0, 1, 0, 0],
    [0, 1, 0, 0, 1],
    [1, 0, 0, 0, 1]
]

chr_caret = [
    [0, 1, 0],
    [1, 0, 1],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

chr_hash = [
    [0, 1, 0, 1, 0],
    [1, 1, 1, 1, 1],
    [0, 1, 0, 1, 0],
    [1, 1, 1, 1, 1],
    [0, 1, 0, 1, 0]
]

chr_backtick = [
    [1, 0],
    [0, 1],
    [0, 0],
    [0, 0],
    [0, 0]
]

chr_tilde = [
    [0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [1, 0, 1, 0, 1],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0]
]

chr_ampersand = [
    [0, 1, 0, 0, 0],
    [1, 0, 1, 0, 0],
    [0, 1, 1, 0, 1],
    [1, 0, 0, 1, 0],
    [0, 1, 1, 0, 1]
]

chr_brace_left = [
    [0, 1],
    [1, 0],
    [1, 0],
    [1, 0],
    [0, 1]
]

chr_brace_right = [
    [1, 0],
    [0, 1],
    [0, 1],
    [0, 1],
    [1, 0]
]

chr_brace_square_left = [
    [1, 1],
    [1, 0],
    [1, 0],
    [1, 0],
    [1, 1]
]

chr_brace_square_right = [
    [1, 1],
    [0, 1],
    [0, 1],
    [0, 1],
    [1, 1]
]

chr_brace_curly_left = [
    [0, 0, 1],
    [0, 1, 0],
    [1, 1, 0],
    [0, 1, 0],
    [0, 0, 1]
]

chr_brace_curly_right = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 1, 1],
    [0, 1, 0],
    [1, 0, 0]
]

chr_greater_than = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
    [0, 1, 0],
    [1, 0, 0]
]

chr_less_than = [
    [0, 0, 1],
    [0, 1, 0],
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]

chr_pipe = [
    [1],
    [1],
    [1],
    [1],
    [1]
]

chr_question_mark = [
    [1, 1, 1],
    [0, 0, 1],
    [0, 1, 1],
    [0, 0, 0],
    [0, 1, 0]
]

chr_semi_colon = [
    [0, 0],
    [0, 1],
    [0, 0],
    [0, 1],
    [1, 0]
]

chr_full_block = [
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1]
]

chr_negation = [
    [0, 0, 0],
    [0, 0, 0],
    [1, 1, 1],
    [0, 0, 1],
    [0, 0, 0]
]

lookup = {
    '0': chr_0, '1': chr_1, '2': chr_2, '3': chr_3, '4': chr_4,
    '5': chr_5, '6': chr_6, '7': chr_7, '8': chr_8, '9': chr_9,
    'a': chr_a, 'b': chr_b, 'c': chr_c, 'd': chr_d, 'e': chr_e,
    'f': chr_f, 'g': chr_g, 'h': chr_h, 'i': chr_i, 'j': chr_j,
    'k': chr_k, 'l': chr_l, 'm': chr_m, 'n': chr_n, 'o': chr_o,
    'p': chr_p, 'q': chr_q, 'r': chr_r, 's': chr_s, 't': chr_t,
    'u': chr_u, 'v': chr_v, 'w': chr_w, 'x': chr_x, 'y': chr_y,
    'z': chr_z,
    'A': chr_a_up, 'B': chr_b_up, 'C': chr_c_up, 'D': chr_d_up,
    'E': chr_e_up, 'F': chr_f_up, 'G': chr_g_up, 'H': chr_h_up,
    'I': chr_i_up, 'J': chr_j_up, 'K': chr_k_up, 'L': chr_l_up,
    'M': chr_m_up, 'N': chr_n_up, 'O': chr_o_up, 'P': chr_p_up,
    'Q': chr_q_up, 'R': chr_r_up, 'S': chr_s_up, 'T': chr_t_up,
    'U': chr_u_up, 'V': chr_v_up, 'W': chr_w_up, 'X': chr_x_up,
    'Y': chr_y_up, 'Z': chr_z_up,
    '.': chr_dot, ' ': chr_space, ':': chr_colon, '=': chr_equals,
    '!': chr_exclamation, ',': chr_comma, '_': chr_underscore, '-': chr_minus,
    '+': chr_plus, '/': chr_forward_slash, '\\': chr_back_slash,
    '*': chr_asterisk, "'": chr_single_quote, '"': chr_double_quote,
    '£': chr_gbp, "$": chr_usd, "€": chr_eur, "%": chr_percent,
    "^": chr_caret, "#": chr_hash, "`": chr_backtick, "~": chr_tilde,
    "&": chr_ampersand, "(": chr_brace_left, ")": chr_brace_right,
    "[": chr_brace_square_left, "]": chr_brace_square_right,
    "{": chr_brace_curly_left, "}": chr_brace_curly_right,
    ">": chr_greater_than, "<": chr_less_than, "|": chr_pipe,
    "?": chr_question_mark, ";": chr_semi_colon, "█": chr_full_block,
    "¬": chr_negation, "@": chr_at
}