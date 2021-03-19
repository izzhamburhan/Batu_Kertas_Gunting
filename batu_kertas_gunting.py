import random

def main() :
    pemain = input("Apa pilihan anda ? 'b' untuk batu , 'k' untuk kertas, 'g' untuk gunting\n" )
    komputer = random.choice(['b','k','g'])

    if pemain == komputer :
        return 'Permainan Seri'


    # r>s , s>p , p>r
    if is_win(pemain, komputer):
        return 'Tahniah, Anda Menang!'

    return 'Maaf, Anda Kalah'

def is_win(player , opponent) :
    #return true kalau player menang
    #b>g , g>k , k>b
    if (player == 'b' and opponent == 'g' ) or (player == 'g' and opponent == 'k' ) \
        or (player == 'k' and opponent == 'b') :
        return True

print(main())