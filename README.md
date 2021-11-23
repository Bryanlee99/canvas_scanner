# Canvas Scanner

A simple script that scans Harvard Canvas URLs to find the course IDs for course pages with particular keywords. Useful for finding past canvas courses that are still publicly accessible and to download their course content and syllabi. The course content must be manually downloaded, but the course numbers are automatically found.

I used this to find past Harvard Chinese courses. In case you're curious, they're:

- 82322 - 120B
- 84239 - 123XB
- 92163 - 130A
- 84401 - 130B
- 92501 - 130XA
- 83828 - 130XB
- 92298 - 140A
- 83376 - 140B
- 92405 - 142A
- 82303 - 142B
- 92195 - 150A
- 83380 - 150B
- 83225 - 163

# Scanner's Approach

The scanner's approach is simple: each canvas URL has a course number as a numerical post-fix (e.g. Chinese 120A, https://canvas.harvard.edu/courses/92342, post-fix 92342). Each course corresponds with a number, and many of these are publicly accessible to students. These URLs are easy to find for currently offerred classes via `my.harvard.edu`, but past semester course pages for courses one wasn't enrolled in aren't easily accessible. These post-fixes are generally incremented per semester (usually covering a range of 10k values per semester). The scanner brute forces each post-fix and makes requests to each URL. If a page is private, no main HTML content will appear. However, if a page is public, then the HTML content is searched for a given keyword. The post-fixes which have this keyword are appended to a list which is printed at the end of operation.

Harvard Canvas sites are either:

- Private: https://canvas.harvard.edu/courses/92340
- Public (current semester): https://canvas.harvard.edu/courses/92342
- Public (past semesters): https://canvas.harvard.edu/courses/82236

This scanner finds public sites, either current or past semesters. Notably, the Harvard Canvas site can only be used by Harvard Key registered students, so the scanner only works with proper cookie credentials. These can be extracted after you login to Canvas once, and the cookies will remain valid for 24 hrs so they will suffice for your requests.

# Usage

Input the `INPUT PARAMETERS` in the header of the `scanner.py` script.

- Course number: scans [`start_course`, `end_course`] post-fixes. Looking at my Harvard canvas page, the semesters are generally Fall 2021 [88000, 95000], Spring 2021 [79000, 88000]. Past course ranges likely continue a similar linear pattern
- Key word: add a key word to find in `key_word`, which is the word to find on non private Canvas pages.
- Cookies: the `cookies_dict` holds the credentials to authenticate the scanner's HTTP requests. Replace the `_csrf_token`, `_legacy_normandy_session`, `canvas_session`, `log_session_id` with the appropriate cookies. These can be found by logging into `canvas.harvard.edu`, authenticating via Harvard Key, and looking at the page's cookies (e.g. inspect the page -> click `storage` tab -> click cookies, on most browsers). The cookies you find should appear similar in format and length to those in the existing `cookies_dict`.

`scanner.py` runs like a normal python script, `python3 scanner.py`.

Scanning 10k pages takes ~1hr. Leave it running in the background.
