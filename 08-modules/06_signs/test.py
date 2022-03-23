"""
Zaimportuj generator bezpośrednio do programu.

"""
import gen_user_input
import seq_finder

seq_finder.print_intro()
generated_str = gen_user_input.gen_form_user()
print('Generated string: ',generated_str)
sequences = seq_finder.finder_seq(list(generated_str))
winner = seq_finder.dict_max_value(sequences)
print(f'Longest seq {winner[0] * winner[1]} --> {winner[1]} ')
