def convert_target(value):
    if( value == 'Obesity_Type_I' or  value == 'Obesity_Type_II' or value == 'Obesity_Type_III'):
        return 'yes'
    return 'no'