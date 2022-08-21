_pad        = '_'
_punctuation = ',.!?-~'
_letters = 'AEINOQUabdefghijkmnoprstuvwyz'
_letters_ipa = 'ʃʧ↓↑ '


# Export all symbols:
symbols = [_pad] + list(_punctuation) + list(_letters) + list(_letters_ipa)

# Special symbol ids
SPACE_ID = symbols.index(" ")