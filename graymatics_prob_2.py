import sys
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
    brack_chars= sys.argv[1]
    print(f'{brackets().order_type(brack_chars)}')
    
