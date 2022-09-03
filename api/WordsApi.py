import http.client


class WordsApi:
    def get_wordlist(self):
        def parse_wordlist(wordlist):
            words = wordlist.replace("\n", "")
            words = ''.join(character for character in words if not character.isnumeric())
            words_tuple = tuple(words.split(" "))
            return words_tuple

        connection = http.client.HTTPSConnection("raw.githubusercontent.com", 443)
        connection.request(
            "GET",
            "/tweedegolf/generatorbundle/master/src/TweedeGolf/GeneratorBundle/Resources/wordlists/polish.list",
            headers={"User-Agent": " 2/0"}
        )

        response = connection.getresponse()
        data = response.read()
        wordlist = parse_wordlist(data.decode())

        return wordlist
