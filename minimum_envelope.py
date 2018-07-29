from functions import findNoteLocations
from functions import closestDistanceBetweenTwoPoints
from functions import closestDistanceBetweenTwoNotes
from functions import printToTab
from functions import closestMelodyNotesDistance




##  two octave C major scale
testNotes = ('C3', 'D3', 'E3', 'F3', 'G3', 'A3', 'B3', 'C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5')



##
##def closestMelodyNotesDistance(testNotes):
##    
####    This function locates all the places on the neck where a note can be played.
####    It then takes the first two notes and finds the minimum distance between them,
####    considering all the places on the neck where they could be played.
####    Using the first pair of notes as a starting point, the next pair is then decided
####    based on the previous value.  In this way, the closest distance is chosen, based
####    on the preceding choice.
##    
####    I think this is called a Greedy Algorithm.  The following definition is from Wikipedia:
##    
####    A greedy algorithm is an algorithmic paradigm that follows the problem solving
####    heuristic of making the locally optimal choice at each stage with the intent of
####    finding a global optimum.
##
##
##    noteLocations = [[]]
##
#### Creates an array of all the notes' locations
##    g=0
##    while g < len(testNotes):
##        noteLocations.append([])
##        noteLocations[g] = findNoteLocations(testNotes[g])
##        g=g+1
##
##
####  Finds the closest distance between every pair of notes
##    notePairs = [[]]
##    notePairs[0] = closestDistanceBetweenTwoNotes(noteLocations[0], noteLocations[1])
##    d=1
##    while d < len(testNotes)-1:
##        notePairs.append(closestDistanceBetweenTwoNotes([notePairs[d-1][2]], noteLocations[d+1]))
##        d=d+1
##        
##        
####  This adds all the individual note pairs to one array
##    testNotesClosestLocations = notePairs[0][1:3]
##    d=1
##    while d < len(testNotes)-1:
##        testNotesClosestLocations.append(notePairs[d][2])
##        d=d+1
##
##    return testNotesClosestLocations
##




testNotesClosestLocations = closestMelodyNotesDistance(testNotes)

printToTab(testNotesClosestLocations)

