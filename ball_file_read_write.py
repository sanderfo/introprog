g = 9.81 # Definerer g først som sist, tyngdeakselerasjon

def funksjon(file): # Funksjon av et inndatasett

    infile = open(file, "r") # Åpner filen vi skal se på

    line = infile.readline() # Leser første linje
    v0 = float(line.split()[1]) #V0 er andre "ord" i første linje

    t = [] # Tom liste for t

    infile.readline() #Skipper linje 2

    for line in infile: #For-løkke for å lese resten av linjene

        T = line.split() # T er en liste med ord per linje
        for i in T: # Nøsta for-løkke her, går gjennom alle ordene i lista
            t.append(float(i)) # Legger til t-verdiene i t og gjør de om til float
    return v0, t # Returnerer v0 og t-verdiene fra datasettet



print(funksjon("ball.dat")) # Printing er gøy

def ty_table(file): # oppgave c), funksjon som lager en tekstfil med et table
    infile = open(file, "r") # Leser filen

    line = infile.readline() # mye av dette er kopiert fra funksjonen over
    v0 = float(line.split()[1])

    t_list = []
    y_list = [] # Egen tom liste for y-verdier her

    infile.readline()

    for line in infile:

        T = line.split()
        for i in T:
            t_list.append(float(i))
    t_list = sorted(t_list) # Her kommer det noe nytt, bruker sorted til å sortere listen i stigende rekkefølge

    for t in t_list: # Løkke for å regne ut y-verdier, legger i egen liste
        y = v0*t-0.5*g*t**2
        y_list.append(y)

    with open("ty_out.txt", "w") as outfile:
        for i in range(len(t_list)): # itererer gjennom t_listen
            outfile.write("t: %2.2f y: %2.5f \n" %(t_list[i], y_list[i])) #skriver til utdatafil, fjerner noen desimaler

ty_table("ball.dat")

def test_read(): # Testfunksjon
    with open("test.txt", "w") as outfile: # Skriver til en fil som beskrevet i b)
        outfile.write("v0: 5.0 \n")
        outfile.write("t: \n") # blir en ganske lik tekstfil som i a)
        outfile.write("0.5 1 2 5 3 7")

    exp_v0 = 5.0
    exp_t = [0.5, 1.0, 2.0, 5.0, 3.0, 7.0]
    comp_v0, comp_t = funksjon("test.txt")
    success = exp_v0 == comp_v0 and exp_t == comp_t
    assert success, "Her er det feil"

test_read()

"""
Terminal > run ball_file_read_write.py
(3.0, [0.15592, 0.28075, 0.36807889, 0.35, 0.57681501876, 0.21342619, 0.0519085, 0.042, 0.27, 0.50620017, 0.528, 0.2094294, 0.1117, 0.53012, 0.372985, 0.39325246, 0.21385894, 0.3464815, 0.57982969, 0.10262264, 0.29584013, 0.17383923])
"""
