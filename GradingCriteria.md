# Grading Criteria Programmieren T3INF1004

## Die Studierenden kennen die Grundelemente der prozeduralen Programmierung. 
#### Algorythmenbeschreibung
Dies ist die Funktion die eine Liste erstellt mit allen Tiles die ein Level hat.
```
 def createLevel(self):
        self.level = list()
        for rowIndex,row in enumerate(self.LevelData):          #Enumerating the level data which comes from a level.txt 
            for colIndex,cell in enumerate(row):                #Using two For loops to be able to a loop thourg the row and b to loop through every column and aswell contain the information where we are
                if cell == 'a':                                 # using a char to set player spawn
                    self.player.spawn.x = colIndex * tilsize
                    self.player.spawn.y = rowIndex * tilsize
                    continue
                if not cell == " ":
                    self.level.append(self.tileManager.createTile(cell, colIndex * tilsize , rowIndex * tilsize)) # we use the information of the position we are in to let the tilemanager create a tile for the level
```
[Link zur Datei](https://github.com/Domidhbw/TimeTheFreeze/blob/main/Level/levelManager.py)
#### Datentypen
Hier ist ein Snippet aus der Player innit Funktion.
Wir haben einen Bool, Integer sowie eine Floating Point number. Es gibt auch noch Strings und Char als Datentypen.
```
    self.hasJump = True
    self.jumpSpeed = -900
    self.friction = 0.2
```
[Link zur Datei](https://github.com/Domidhbw/TimeTheFreeze/blob/main/player/player.py)
#### E/A-Operationen und Dateiverarbeitung
Wir haben in unserem Projekt eine Json Datei eingelesen und diese dann genutzt um zu speichern welche Levels schon geschafft sind und welche nicht.
Der erste Code Zeigt die Json und der zweite Zeigt wie die Daten der Json eingelesen werden.
Der Dritte Code Zeigt wie mit den Eingelesenen Daten gearbeitet wird um eine Liste der Levels zu erstellen welche Spielbar sind.
```
{
    "levels": {
        "1": true,
        "2": true,
        "3": true,
        "4": true,
        "5": true,
        "6": true,
        "7": true,
        "8": true
    }
}
```
```
def loadLevelStatus(self):
        try:
            with open(self.saveFilePath, 'r') as file:
                data = json.load(file)
                return data['levels']
        except FileNotFoundError:
            return {}
```
```
def getLevels(self,getSelectables):
    if getSelectables:
        selectableLevels = []
        for level,completed in self.levelStatus.items():
            self.possibleLevels.append(level)
            if completed == True:
                selectableLevels.append(level)
        return selectableLevels
    else:
        unSelectableLevels = []
        for level,completed in self.levelStatus.items():
            if completed == False:
                unSelectableLevels.append(level)
        return unSelectableLevels
```
[Link zur Datei](https://github.com/Domidhbw/TimeTheFreeze/blob/main/Menu/menu.py)
#### Operatoren
Dies ist ein Auszug aus dem Player movement. Hier werden Vergleichsoperatoren verwendet aber auch Arithmetische Operatoren.
```
def applyFriction(self):
    if self.direction.x > 0.1:
        self.direction.x -= self.friction
    if self.direction.x < -0.1:
        self.direction.x += self.friction
```
[Link zur Datei](https://github.com/Domidhbw/TimeTheFreeze/blob/main/player/player.py)
#### Kontrollstrukturen
Dies ist die Logik für die verschiedenen Game States. Eine while loop läuft konstant, innerhalb von ihr passiert jede logik währen des Spieles.
Die einzelnen if statements schauen welcher GameState gerade am laufen ist und entscheiden anhand daran was zu tun ist.
```
while running:
    #GET INPUT
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            running = False
        elif gameState == levelSelection:
            if event.type == pygame.MOUSEBUTTONDOWN:
                gameState = menu.handleMouse(pygame.mouse.get_pos(),levelManager,player)
        elif gameState == playing:
            if keys[pygame.K_w]:
                superPower.doIt(player,levelManager)
            if keys[pygame.K_ESCAPE]:
                gameState = escape
        elif gameState == escape:
            if event.type == pygame.MOUSEBUTTONDOWN:
                gameState = escapeMenu.handleInput(pygame.mouse.get_pos(),player,levelManager)
        elif gameState == 'quit':
            running = False
```
[Link zur Datei](https://github.com/Domidhbw/TimeTheFreeze/blob/main/Main.py)
#### Funktionen
Hier ist die Logik des playing States. Es werden eigene Funktionen der selbst erstellten Objekten abgerufen jeden Frame um das Spiel zu updaten und zu malen. Die verschiedene Objekte bekommen hier Informationen und zugriff auf andere Objekte aber auch auf die Variable dt (short for DeltaTime) welche da ist damit alles Frame Independent funktionieren kann.
```
if gameState == playing:
        musicHandler.playTrack(0,False)
        screen.fill("darkgrey")
        #GAMELOOP  
        player.update(levelManager)
        levelManager.update(player,dt)
        collision.update(player,levelManager.collisionMap,dt)

        #DRAW THE GAME
        screen.blit(background,(0,0)) 
        levelManager.drawLevel(screen)
        player.draw(screen)
```
[Link zur Datei](https://github.com/Domidhbw/TimeTheFreeze/blob/main/Main.py)
#### Stringverarbeitung
Hier wird eine txt datei eingelesen die als großer Sring behandelt wird welcher verarbeitet wird zu einer liste damit man daraus das level auslesen kann.
```
def loadNewLevel(self,level):
    self.currentLevel = level
    filePath = './Levels/level' + str(level) + '.txt'
    if int(self.currentLevel) < 7:
        with open(filePath, 'r') as file:
            # Read lines without stripping
            level = [line.rstrip('\n') for line in file]
        self.LevelData = level
```
[Link zur Datei](https://github.com/Domidhbw/TimeTheFreeze/blob/main/Level/levelManager.py)
#### Strukturierte Datentypen
Siehe Beispiel Algorythmenbeschreibung, Dort werden Tiles einer Liste hinzugefügt die dann genutzt wird um effizient das Level zu laden aber auch um Collision zu checken. Die Tiles selber haben dann Informationen über Position aussehen etc.

### Sie können die Syntax und Semantik von Python sowie Sie kennen verschiedene Datenstrukturen und können diese exemplarisch anwenden.
Syntax:
Ich bin besonders stolz auf die Art und Weise wie die Levels erstellt werden und wie jeder Block ein eigenes Tile Objekt ist. Dies ermöglicht es nämlich einfach neue Levels zu laden aber auch entscheiden zu können ob ein block eine Hitbox hat oder keine Hitbox und nur als Deko dient. Auch wie die Tiles in den levels.txt Dateien abgespeichert sind. Dies hat mir es nämlich ermöglicht mit einem eigenen Level Editor leicht und schnell Levels zu bearbeiten sowie zu erstellen.
Den ganzen Code zu zeigen wäre etwas viel deshalb zeige ich hier wie die Collisions gehandelt werden da man daran erkennen kann wie praktisch die tiles sind da es sehr leicht ist zu differenzieren ob etwas von unten, von oben oder von der Seite getroffen hat.

Datenstrukturen:
Im unteren Code wurden Listen benutzt um die Tile Objekte zu speichern. Es wurde auf Vektoren zugegriffen um die Richtung der Collision abzufragen. Es wurde auch die Python eigene rect Datenstruktur genutzt um den Spieler auf die richtige Seite eines Tiles zu stellen.
```
 def horizontalMovementCollisions(self,dt):
        self.player.applyFriction()
        self.player.move(dt)         
        player_points = [self.player.rect.bottomleft, self.player.rect.bottomright]
        for tile in self.collisionMap:
            if any(tile.rect.collidepoint(point) for point in player_points):
                self.checkForKillTiles(tile.char)
            if tile.rect.colliderect(self.player.rect):
                if self.player.direction.x < 0:
                    self.player.rect.left = tile.rect.right
                elif self.player.direction.x > 0:
                    self.player.rect.right = tile.rect.left
                if tile.char == 'e':
                    self.playerJumpTile()
                if tile.char == 'f':
                    self.levelManager.loadNextLevel()
                    self.player.die(self.levelManager)
    
    def verticalMovementCollisions(self,dt):
        self.player.applyGravity(dt)
        for tile in self.collisionMap:
            if tile.rect.colliderect(self.player.rect):
                if self.player.direction.y > 0:
                    self.player.direction.y = 0
                    self.player.rect.bottom = tile.rect.top
                    self.player.hasJump = True
                elif self.player.direction.y < 0:
                    self.player.rect.top = tile.rect.bottom
                    self.player.direction.y = 0
                if tile.char == 'e':
                    self.playerJumpTile()
```
### Sie können ein größeres Programm selbständig entwerfen, programmieren und auf Funktionsfähigkeit testen (Das Projekt im Team) (10)
[Link zu Davids Commit](https://github.com/Domidhbw/TimeTheFreeze/commit/a09f26ced5ee4087e1c16134e656260244bbc1ff)
[Link zu Dominiks Commit](https://github.com/Domidhbw/TimeTheFreeze/commit/e5574dc1ecf1fa079e9a6ca77606dee2534c40a1)
Dies sind zwei Commits die gegen Ende des Projekts entstanden sind. Ganz unten beim Punkt unsere Probleme gehen wir mehr auf Git ein. 
## METHODENKOMPETENZ (10 Punkte)
Ich habe vscode als code Umgebung genutzt um Code zu schreiben aber auch zum debuggen.
![VSC](png\VSCode.png)

Ich habe GitHub Desktop genutzt um mir für einzelne Experimente einen neuen Branch zu erstellen aber auch zum Commiten.
![Git](png\githubDesktop.png)
## PERSONALE UND SOZIALE KOMPETENZ (20 Punkte)
### Die Studierenden können ihre Software erläutern und begründen. (5)
![Git](png\hilfe.png)
Hier hat mich Noah gefragt wie ich meine Dateien einlese da er Probleme hatte Text Dateien in Python einzulesen.
### Sie können existierenden Code analysieren und beurteilen. (5)
Datei wurde extra abgegeben. grading_pyPoll.md
### Sie können sich selbstständig in Entwicklungsumgebungen und Technologien einarbeiten und diese zur Programmierung und Fehlerbehebung einsetzen. (10)
Wir haben uns Pygame beigebracht welches die Haupt Bibliothek war mit der wir unser Spiel geschrieben haben. Außerdem haben wir gelernt wie man Json nutzen kann um daten extern zu speichern. 
Hilfe haben wir uns geholt wo wir zu dumm waren weil wir immer an der falschen stelle geschaut haben. 
![Git](png\help.png)

## ÜBERGREIFENDE HANDLUNGSKOMPETENZ (30 Punkte)
### Die Studierenden können eigenständig Problemstellungen der Praxis analysieren und zu deren Lösung Programme entwerfen (30)
Wir sind stolz auf das gesammte Projekt weil wir beide das erste mal ein größeres Spiel entwickelt haben welches auch Graphiken, Musik und eine Eigene Mechanik besitzt. Zudem auch darüber das wir viel miteinander Kommuniziert haben und das Projekt aufteilen konnten und uns beide auf Sachen konzentrieren konnten die uns besonders viel Spaß machen. Für David ist das die Musik gewesen. Sowie das Player Movement.
Zum Player:
Der Player bekommt im Konstruktor Informationen darüber wie er Aussieht. Er bekommt auch feste Werte für seinen Sprung für die Physik und viele Werte darüber ob er gerade Springen darf, seine power nutzen darf, am leben ist etc.
Der Input des Players passiert in der getKeyPressed Funktion. Hier wird der Direction Vector des Players in die Richtung des gedrückten Knopfs angepasst wodurch die eigentliche Bewegung des Players in eine andere Funktion ausgelagert werden kann.
Auch ob er springen oder Sprinten soll wird hier entschieden.
Der Aufruf dieser Funktion passiert in der Update Funktion des Spielers. 
Der Spieler selbst wird in der move Funktion bewegt. Hier wird dann der Wert seiner Geschwindigkeit mit dem Direction Vector multipliziert und auch mit der dt Variable. Diese Sorgt dann dafür das der Spieler sich frame Independent bewegt. Andere Coole Funktionen sind die applyFriction sowie applyGravity funktion. Die applyFriction sorgt dafür das der Spieler nicht Sofort stoppt sondern ein minimales abbremsen hat. Die applyGravity sorgt dafür das der Spieler ein realistisches Fall Gefühl bekommt. Die Funktionen sind nicht sehr besonders vom Coding aber sie haben viel Zeit beansprucht um die Richtigen werte zu bekommen welche dann dafür sorgen das sich das Spiel richtig anfühlt.
Hier Code des Player movments einfügen Sowie Verlinkung zu den Ordnern.
[Link zur Datei](https://github.com/Domidhbw/TimeTheFreeze/blob/main/player/player.py)
[Link zur Datei](https://github.com/Domidhbw/TimeTheFreeze/tree/main/music)

Für Dominik ist das das Collision managment und die Level Struktur.
Wie die Levels Geladen werden und was daran so cool ist wurde weiter oben beschrieben weswegen ich hier nicht auf den Code eingehen möchte sondern warum es mir so sehr gefällt. Das ist zum einem weil es sehr Praktisch ist was sich während des Projekts mehrfach bewiesen hat. Ich konnte einfachen meinen Level Editor Nils schicken (Welcher Für uns das Design gemacht hat.) dieser konnte dann ausprobieren wie groß etwas im Spiel sein muss und wie es Später aussieht. Was auch sehr praktisch dran ist, ist wie leicht wir levels alle untereinander austauschen konnten da es nur eine txt war und wir dadurch vieles ausprobieren konnten. Nun aber zum Collision managment. Da bin ich stolz drauf weil es Ewigkeiten gebraucht hat bis es gut funktioniert hat. Viele Probleme hatten wir damit das die Collsision zu früh entstanden ist oder zum Teil der Spieler auf die falsche Seite eines Blockes gefallen ist. Und auch als sie fertig war sind immer wieder Kleinigkeiten aufgetreten. Die Besonderheit war es hier die richtige Reihenfolge zu haben. Zum Beispiel wird der Player erst kurz vor Collision Checks bewegt damit nichts sich doch noch bewegt da wir auch eine Kamera hatte die in Bewegung jeden Block bewegt hat und den Spieler stoppen musste. Nun genauer zur horizontalMovementCollision. Hier erstellen wir nachdem wir den Spieler bewegt haben Punkte damit die Collision schneller reagiert, dies wurde hinzugefügt nachdem aufgefallen ist das der Spieler im fall zum Falschen zeitpunkt stirbt mit den anderen Collsision checks. Danach gehen wir alle Tiles durch in unserer Collision Map und Reagieren dementsprechend, heißt wenn der Spieler irgendwo einen Punkt der kill Tiles berührt stirbt er und wenn er ein anderen teil von der Seite berührt wird er dementsprechen an die richtige Seite platziert damit er nicht durch kommt. In der VerticalMovementCollision passiert an sich das gleiche nur wird der spieler eben oben oder unten Platziert und seine y Richtung muss auch null gesetzt werden sonst kann er bei zu langem stehen plötzlich durch die map glitchen. In beiden Checks kann man auch special Tiles hinzufügen durch welche das nächste Level geladen werden oder eben die Sprungplatform aktiviert wird.
[Link zur Datei](https://github.com/Domidhbw/TimeTheFreeze/blob/main/collisionHandler.py)

Unsere Probleme:
Wir hatten kein Problem mit der Timeline da wir uns am Anfang dafür entschieden haben zu erst an Movement und Logik zu arbeiten bis wir dann eben Levels machen und ein Menü hinzufügen. Wir hatten dann beide jeden Tag dran gearbeitet und Rücksprache gehalten ob wir im Zeitplan sind und uns einmal die Woche getroffen um neben einander am Projekt zu arbeiten. Dies hat uns zwar Zeit gekostet da wir alleine wahrscheinlich Produktiver gewesen wären aber es hat uns die Möglickeit gegeben entscheidungen zeitgleich zu treffen wodurch wir beide immer ganz genau wussen wohin sich das Spiel entwickeln soll und was wann zu machen ist.
Eines unseren ganz großen Probleme war aber Davids Internet und Laptop. Sein Internet ist Grundlegend sehr schlecht wodurch viele Discord Übertragungen abgebrochen wurden und man sich über Mobilfunk durchkämpfen musste. Das hat dafür gesorgt das Dominik kaum bis gar nicht bei Git Problemen helfen konnte dies betrifft vorallem Commits und Merging am Anfang. Dadurch wurde vieles über Dominiks Git Commited die Dateien wurden sich dann über Discord zugeschickt und im Mobilfunk Telefonat erklärt wo was hingehört. Dadurch war es aber auch jedes mal noch besser wenn dann der Code Funktioniert hat.  