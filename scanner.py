import requests

# INPUT PARAMETERS
key_word = "Chinese"
start_course = 85000
end_course = 95000
cookies_dict = {
    "_csrf_token": "XqfaTd33sKhKUTX%2FOzjJ8MPMTo5YGbvb0PHGDixXuL0kzYw%2FpaXxhyECRZ5LCp3IpYcl%2BjAu15eWlvBrSzPs9w%3D%3D",
    "_legacy_normandy_session": "fyZNJjBWyos2lRn5ZOraUw+aw4MDbzbgfXGtFLrGWH6ybeA7raCr3vOlInQEYX2QUPizplA-KZZyu3CXXqKFme_YQly57CFXYSSJLxi2W2gMnutLhACcFWch4Tlz-qA_5psJBgppbVVUjxgNCnBnIcuqZpUvA4dkWD__q6hHcoSSPJpjsmgE0SShlv-5i2JapN-lWzkVEo8o1OX7f_H1HCKqM_TanyBBfMs5UBjlw2EoAv3ntaU_yspzyHaJe8nvZlY_DjJS5SWcscr42OGwkFH6WiqHdTsT2E7E3OCq2b0anuCxww5HCT9OPbu9v6LR1D6Wh5UEyC8adJcb-CIpYvaxK8wE0IT7U0FWGrnvtuZ-c-BvGxaDmwfsQIUP8hd7-TomuNBHaxo-tFJdNYv5CCjCHKgPA6sOv7SzJwOfp_uba8Ao7IxWoncbA3W0DQX0AHINZti4j4JeHe61SIRh8UsPJBnYGlEyStyyGFb3xa1vHGuOFLRcFy_KxTH874B5Yn3_rqJznQKHceJFFQ2wOWR.4WlahcNqujTphtaWSgeM_w-ZX1o.YZUQgw",
    "canvas_session": "fyZNJjBWyos2lRn5ZOraUw+aw4MDbzbgfXGtFLrGWH6ybeA7raCr3vOlInQEYX2QUPizplA-KZZyu3CXXqKFme_YQly57CFXYSSJLxi2W2gMnutLhACcFWch4Tlz-qA_5psJBgppbVVUjxgNCnBnIcuqZpUvA4dkWD__q6hHcoSSPJpjsmgE0SShlv-5i2JapN-lWzkVEo8o1OX7f_H1HCKqM_TanyBBfMs5UBjlw2EoAv3ntaU_yspzyHaJe8nvZlY_DjJS5SWcscr42OGwkFH6WiqHdTsT2E7E3OCq2b0anuCxww5HCT9OPbu9v6LR1D6Wh5UEyC8adJcb-CIpYvaxK8wE0IT7U0FWGrnvtuZ-c-BvGxaDmwfsQIUP8hd7-TomuNBHaxo-tFJdNYv5CCjCHKgPA6sOv7SzJwOfp_uba8Ao7IxWoncbA3W0DQX0AHINZti4j4JeHe61SIRh8UsPJBnYGlEyStyyGFb3xa1vHGuOFLRcFy_KxTH874B5Yn3_rqJznQKHceJFFQ2wOWR.4WlahcNqujTphtaWSgeM_w-ZX1o.YZUQgw",
    "log_session_id": "e9c706726b5ee59fda44fa9f545368c6"
}

# Main code
correct = []
for i in range(start_course, end_course):
    r =requests.get(f'https://canvas.harvard.edu/courses/{i}', cookies=cookies_dict)
    if r.text.find(key_word) != -1:
        correct.append(i)
        print(f"Found {i}")
    if i % 50 == 0:
        print(f"Processed Course {i}")

print(correct)


# Miscellaneous Chinese Courses
# 82322 - 120B
# 84239 - 123XB
# 92163 - 130A
# 84401 - 130B
# 92501 - 130XA
# 83828 - 130XB
# 92298 - 140A
# 83376 - 140B
# 92405 - 142A 
# 82303 - 142B
# 92195 - 150A
# 83380 - 150B
# 83225 - 163

# [86490, 86846, 86876, 86940, 86947]
# [82096, 82209, 82236, 82303, 82322, 82353, 82516, 82960, 83084, 83085, 83225, 83376, 83380, 83799, 83800, 83828, 83873, 83876, 84239, 84271, 84338, 84401, 84559, 84560, 84847, 84958, 84959, 84969, 84984, 85017, 85032, 85043, 85045, 85200, 85426]