from src.generator import MusicGenerator
from src.player import MusicPlayer

if __name__ == "__main__":
    # Step 1: Generate music
    generator = MusicGenerator(tempo=140, notes=30)
    filepath = generator.generate("my_song.mid")
    print(f"✅ Music generated: {filepath}")

    # Step 2: Play music
    player = MusicPlayer()
    player.play(filepath)
