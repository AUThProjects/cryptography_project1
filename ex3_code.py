from operator import itemgetter

# Dictionary on Greek letters-ints
let_to_int = {}
int_to_let = {}

for i in range (25):
    if 913+i > 930:
        let_to_int[chr(913+i)] = i-1
        int_to_let[i-1] = chr(913+i)
    elif 913+i == 930:
        continue
    else:
        let_to_int[chr(913+i)] = i
        int_to_let[i] = chr(913+i)


# Construct Greek Uppercase letters list
greek_uppercase = []

for key in let_to_int:
	greek_uppercase.append(key)

greek_uppercase = sorted(greek_uppercase)

# Computation of Index of Coincidence for given array of letters
def compute_greek_IC(letter_array, letters_length):
    sum = 0
    for i in range(24):
        sum += letter_array[i]*(letter_array[i]-1)/(letters_length*(letters_length-1))
    return sum

# Greek_IC as given in exercise input
greek_ic = 0.069

# Decryption function
def vigenere_decrypt(target_freqs, input):
    nchars = 24 # number of uppercase characters in Greek alphabet
    ordA = let_to_int['Α']
    sorted_targets = sorted(target_freqs)
 
    # Calculates frequences for each letter inside the text
    def frequency(input):
        result = [[c, 0.0] for c in greek_uppercase]
        for c in input:
            result[let_to_int[c] - ordA][1] += 1
        return result
 
    # Calculates correlation of characters in text and statistical distribution
    def correlation(input):
        result = 0.0
        freq = frequency(input)
        freq.sort(key=itemgetter(1))
 
        for i, f in enumerate(freq):
            result += f[1] * sorted_targets[i]
        return result
 
    cleaned = input
    best_len = 0

    # Find the key length that was used to Vigenere Cipher
    found = False
    while not found:
        for key_length in range(2, len(cleaned)):
            subtexts = []
            for i in range(key_length):
                column = []
                j = 0
                while i+j < len(cleaned):
                    column.append(cleaned[i+j])
                    j += key_length
                if len(column) == 1 :
                    break;
                subtexts.append(column)
            for column in subtexts:
                # print(column)
                frequencies = [0] * 24
                for i in range(len(column)):
                   frequencies[let_to_int[column[i]] - let_to_int['Α']] += 1
                for i in range(24):
                    frequencies[i] *= 100/len(column)
                # print(frequencies)
                # print(sum(frequencies))
                column_ic = compute_greek_IC(frequencies,100)
                # print(column_ic)
                if abs(column_ic - greek_ic) < 0.001 :
                    found = True;
                    best_len = key_length
                    print("Found k: " + str(key_length))
                    break;
            if found:
                break

    # Exit if no length is found to satisfy the constraint
    if best_len == 0:
        return ("Text is too short to analyze", "")
 
    # Re-create the frequencies table
    pieces = [[] for _ in range(best_len)]
    for i, c in enumerate(cleaned):
        pieces[i % best_len].append(c)
 
    freqs = [frequency(p) for p in pieces]
 
    # Find best match
    key = ""
    for fr in freqs:
        fr.sort(key=itemgetter(1), reverse=True)
 
        m = 0
        max_corr = 0.0
        for j in range(nchars):
            corr = 0.0
            c = ordA + j
            for frc in fr:
                d = (let_to_int[frc[0]] - c + nchars) % nchars
                corr += frc[1] * target_freqs[d]
 
            if corr > max_corr:
                m = j
                max_corr = corr
 
        key += int_to_let[m + ordA]
 
    r = (int_to_let[(let_to_int[c] - let_to_int[key[i % best_len]] + nchars) % nchars + ordA] for i, c in enumerate(cleaned))
    return (key, "".join(r))
 
 
def main():
    encoded = """ΕΝΠΠΧΙΦΤΔΛΠΞΝΑΒΧΛΟΨΙΟΓΖΩΠΖΓΓΔΚΑΚΑΑΝΜΦΕΔΟΡΑΤΒΔΩΥΟΩΙΝΥΗΑΠΡΜΩΔΥΨΠΡΕΡΟΛΕΝΑΤΤΑΙΤΤΡΡΡΟΛΕΝΑΤΓΑΚΛΣΗΑΛΩΑΛΦΡΗΣΝΨΛΟΥΨΔΑΔΛΚΓΑΑΗΙΚΨΨΙΜΟΔΥΨΖΖΘΑΔΧΩΓΛΘΥΙΛΝΞΛΣΙΖΖΒΚΛΒΣΚΤΙΑΙΝΣΓΛΔΕΙΝΣΒΟΔΧΙΝΣΖΦΨΦΨΙΙΨΖΥΓΞΕΕΚΡΦΝΕΔΗΒΟΛΟΞΩΑΛΕΟΡΓΖΑΩΡΕΘΜΩΤΟΨΙΑΒΚΩΗΚΦΑΤΨΟΛΧΝΩΨΜΗΔΟΔΗΞΟΙΠΕΘΑΤΔΛΟΨΣΝΓΘΧΩΧΝΗΑΦΥΙΕΔΚΓΣΤΖΖΒΠΨΖΘΥΦΨΘΖΧΟΛΕΝΑΤΕΙΙΑΔΩΨΘΥΚΟΦΝΚΧΡΩΗΑΓΗΘΥΓΟΒΗΙΖΚΖΔΥΓΤΝΤΖΨΔΔΤΚΧΥΤΖΜΛΘΣΣΤΙΗΙΖΚΠΣΝΑΤΩΚΠΦΟΟΑΧΙΔΛΡΔΕΘΥΙΤΙΧΤΒΜΗΑΑΡΓΖΑΗΛΑΡΠΧΙΣΤΙΓΕΘΥΙΡΞΜΑΕΠΖΓΝΦΗΣΕΩΨΙΦΨΔΕΛΣΝΕΑΓΑΩΚΑΝΓΣΑΒΦΙΚΤΛΑΓΟΙΘΝΘΤΖΧΨΑΙΙΑΚΤΟΔΕΧΟΔΟΧΦΤΦΗΒΡΓΤΛΒΑΙΟΓΦΜΠΥΝΟΒΗΣΖΑΔΣΑΜΚΡΝΠΨΔΛΣΛΕΚΑΔΖΟΚΑΣΧΨΘΜΜΟΛΧΡΖΙΝΣΓΛΒΧΤΜΑΤΤΣΝΜΧΣΚΡΜΘΜΜΥΝΤΙΧΤΒΣΚΡΒΙΤΥΗΖΓΡΖΤΕΕΚΡΦΗΤΟΥΚΡΓΝΤΔΛΠΥΤΡΓΛΤΧΥΙΩΨΛΤΖΨΝΝΞΜΟΓΛΒΤΨΓΒΩΑΥΤΠΣΝΩΔΟΔΛΘΣΜΟΑΡΓΣΦΨΑΦΦΤΣΛΒΛΥΝΜΧΧΥΤΙΙΑΛΕΩΔΝΡΗΦΕΩΛΟΡΚΒΣΚΡΥΤΖΣΣΥΥΙΑΨΓΥΔΤΣΓΞΛΗΥΖΕΘΓΣΜΠΔΒΧΕΩΡΖΖΒΧΤΒΑΕΟΒΗΙΝΣΙΥΝΙΝΘΜΠΔΓΡΚΘΛΛΥΙΦΤΒΣΨΛΦΓΖΣΣΚΟΝΨΤΟΙΙΕΙΔΨΚΙΙΔΨΗΨΚΟΑΛΡΝΚΘΤΩΔΥΤΠΣΝΥΔΖΕΨΒΑΦΑΥΝΜΜΕΚΡΦΝΗΑΡΟΒΡΝΚΒΟΗΑΤΘΤΙΟΚΡΦΡΚΒΔΥΩΡΓΝΩΤΠΘΑΡΓΣΖΖΧΙΖΝΧΤΧΨΣΝΕΘΣΛΨΟΧΤΒΤΧΨΝΘΦΧΝΥΤΙΚΣΚΙΙΛΔΗΨΛΤΩΔΙΕΨΜΕΙΡΚΦΤΑΑΑΖΑΦΤΚΧΧΔΝΦΜΜΗΦΚΟΧΤΒΟΒΛΠΝΠΣΘΖΖΦΗΙΣΕΘΑΩΨΤΖΟΑΛΡΗΙΚΑΤΤΨΙΣΖΟΓΛΒΡΟΧΡΠΨΩΦΙΓΟΔΕΙΤΓΦΙΠΡΕΘΜΩΑΛΕΘΑΝΡΝΥΗΝΘΛΧΣΥΚΦΠΓΣΛΠΦΝΦΝΩΝΑΛΤΓΜΝΝΧΕΘΑΤΖΘΘΚΩΜΗΦΙΠΦΙΨΨΒΤΧΨΩΝΦΓΟΙΧΡΝΤΦΕΒΗΨΖΞΖΗΚΡΦΡΗΘΤΧΕΙΓΕΡΝΓΛΒΝΔΘΜΠΥΡΝΞΜΗΚΡΒΗΓΥΜΧΡΕΜΗΩΜΖΖΕΗΤΖΕΩΔΓΝΤΝΤΩΛΝΧΤΜΟΓΧΔΕΓΡΝΠΨΠΕΣΙΩΔΛΩΡΕΙΙΙΧΝΑΣΖΓΛΨΙΦΔΡΝΗΛΡΠΓΡΝΗΑΔΡΓΖΑΩΣΔΩΤΜΑΥΨΨΖΜΝΣΚΡΥΝΝΘΣΗΑΔΒΨΚΕΩΧΨΑΙΖΑΡΛΒΝΗΒΖΥΤΣΝΓΖΑΜΖΤΝΔΒΖΥΤΙΥΣΘΥΙΛΦΥΛΡΠΖΖΒΖΨΣΥΚΑΔΖΚΘΥΓΟΙΧΙΝΝΥΦΝΜΖΩΝΠΒΝΨΚΒΖΥΔΓΡΑΜΩΘΤΦΤΖΣΣΤΖΒΗΞΟΙΠΞΝΑΨΒΝΠΤΩΝΛΣΤΖΒΝΕΤΛΜΠΕΟΖΚΔΕΖΨΝΒΓΣΣΑΛΡΗΑΛΣΑΦΟΕΙΜ"""
    greek_ab_freq = [
		12, 0.8, 2, 1.7, 8, 0.5, 2.9, 1.3, 7.8, 4.2, 3.3, 4.4, 7.9, 0.6, 9.8, 5.024, 5.009, 4.9, 9.1, 4.3, 1.2, 1.4, 0.2, 1.6
	]
 
    (key, decoded) = vigenere_decrypt(greek_ab_freq, encoded) # maybe divide by 100
    print("Key:", key)
    print("\nText:", decoded)
 
main()
