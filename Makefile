all	:
		cp challenge01.py challenge01
		cp challenge02.py challenge02
		cp challenge03.py challenge03
		cp challenge04.py challenge04
		cp challenge05.py challenge05
		cp challenge06.py challenge06
		cp challenge07.py challenge07
		cp challenge08.py challenge08
		cp challenge09.py challenge09
		cp challenge10.py challenge10
		cp challenge10.py challenge12
		cp challenge10.py challenge13
		cp challenge10.py challenge14


clean	:
		rm -f challenge01
		rm -f challenge02
		rm -f challenge03
		rm -f challenge04
		rm -f challenge05
		rm -f challenge06
		rm -f challenge07
		rm -f challenge08
		rm -f challenge09
		rm -f challenge10
		rm -f challenge12
		rm -f challenge13
		rm -f challenge14

fclean	:	clean
		rm -f *~

re	:	fclean all
