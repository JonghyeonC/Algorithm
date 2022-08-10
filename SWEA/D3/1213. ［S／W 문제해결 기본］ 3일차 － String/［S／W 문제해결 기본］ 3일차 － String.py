for tc in range(1, 10+1):
    num = int(input())
    word_find = input()
    sen = input()
    word_list = list(map(str, sen.split(word_find)))
    print(f'#{tc} {len(word_list) - 1}')