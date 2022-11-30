class brackets:
   def order_type( self, brack_chars ):
    
       brack_chars=brack_chars.replace(" ", "")
       while True:
           if '[]' in brack_chars :
               brack_chars = brack_chars.replace ( '[]' , '' )
           elif '()' in brack_chars :
               brack_chars = brack_chars.replace ( '()' , '' )
           elif '{}' in brack_chars :
                brack_chars = brack_chars.replace ( '{}' , '' )   
           else :
               return not brack_chars

if __name__ == '__main__':
   brack_chars = '( ) [ ]{ }'
   print(f'{brackets().order_type(brack_chars)}')
   brack_chars1 = '( [ )]'
   print(f'{brackets().order_type(brack_chars1)}')
   brack_chars2 = '{{[]( }})'
   print(f'{brackets().order_type(brack_chars2)}')
   brack_chars3 = '{[() ]}'
   print(f'{brackets().order_type(brack_chars3)}')
   brack_chars4 = '{{[]( )}}'
   print(f'{brackets().order_type(brack_chars4)}')