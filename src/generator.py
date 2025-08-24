from midiutil import MIDIFile
import random
import os

class MusicGenerator:
    def __init__(self, tempo=120, notes=20, output_dir="music"):
        self.tempo = tempo
        self.notes = notes
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    def generate(self, filename="generated_music.mid"):
        midi = MIDIFile(1)
        midi.addTempo(0, 0, self.tempo)

        for i in range(self.notes):
            note = random.randint(60, 72)   # C4–B4 range
            midi.addNote(0, 0, note, i, 1, 100)

        filepath = os.path.join(self.output_dir, filename)
        with open(filepath, "wb") as f:
            midi.writeFile(f)

        return filepath
