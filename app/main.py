
from dotenv import load_dotenv

from synth.note import Note
from synth.music_composer import MusicComposer
from synth.sound_engine import SoundEngine


retro_sequence = [
    # Intro arpeggio
    {"notes": [Note.C4], "duration": 0.2},
    {"notes": [Note.E4], "duration": 0.2},
    {"notes": [Note.G4], "duration": 0.2},
    {"notes": [Note.C5], "duration": 0.2},
    {"notes": [Note.G4], "duration": 0.2},
    {"notes": [Note.E4], "duration": 0.2},
    # Quick repeating bass line
    {"notes": [Note.C3], "duration": 0.3},
    {"notes": [Note.G2], "duration": 0.3},
    {"notes": [Note.F3], "duration": 0.3},
    {"notes": [Note.G2], "duration": 0.3},
    # Main melody
    {"notes": [Note.C4, Note.E4], "duration": 0.4},
    {"notes": [Note.G4, Note.B4], "duration": 0.4},
    {"notes": [Note.A4, Note.C5], "duration": 0.4},
    {"notes": [Note.F4, Note.A4], "duration": 0.4},
    # Rising tension
    {"notes": [Note.G3, Note.B3, Note.D4], "duration": 0.2},
    {"notes": [Note.A3, Note.C4, Note.E4], "duration": 0.2},
    {"notes": [Note.B3, Note.D4, Note.F4], "duration": 0.2},
    {"notes": [Note.C4, Note.E4, Note.G4], "duration": 0.2},
    # Loop back to bass
    {"notes": [Note.C3], "duration": 0.3},
    {"notes": [Note.G2], "duration": 0.3},
    {"notes": [Note.F3], "duration": 0.3},
    {"notes": [Note.G2], "duration": 0.3},
]

murky_dungeon = [
    # Intro with mysterious descending arpeggio
    {"notes": [Note.C4], "duration": 0.3},
    {"notes": [Note.D4], "duration": 0.3},
    {"notes": [Note.B3], "duration": 0.3},
    {"notes": [Note.G3], "duration": 0.3},
    {"notes": [Note.F3], "duration": 0.3},
    {"notes": [Note.E3], "duration": 0.3},
    # Slow, deep bass line
    {"notes": [Note.C2], "duration": 0.5},
    {"notes": [Note.G2], "duration": 0.5},
    {"notes": [Note.F2], "duration": 0.5},
    {"notes": [Note.G2], "duration": 0.5},
    # Main melody with eerie, unstable intervals
    {"notes": [Note.D4, Note.F4], "duration": 0.6},
    {"notes": [Note.E4, Note.G4], "duration": 0.6},
    {"notes": [Note.C4, Note.E4], "duration": 0.6},
    {"notes": [Note.D4, Note.F4], "duration": 0.6},
    # Tension build-up with dissonance
    {"notes": [Note.F3, Note.A3, Note.D4], "duration": 0.3},
    {"notes": [Note.G3, Note.B3, Note.D4], "duration": 0.3},
    {"notes": [Note.E3, Note.G3, Note.B3], "duration": 0.3},
    {"notes": [Note.C3, Note.E3, Note.G3], "duration": 0.3},
    # Return to slow bass and deepen atmosphere
    {"notes": [Note.C2], "duration": 0.5},
    {"notes": [Note.G2], "duration": 0.5},
    {"notes": [Note.F2], "duration": 0.5},
    {"notes": [Note.G2], "duration": 0.5}
]

the_sunset_sequence = [
    # Calm and peaceful intro with light arpeggio
    {"notes": [Note.C4], "duration": 0.3},
    {"notes": [Note.E4], "duration": 0.3},
    {"notes": [Note.G4], "duration": 0.3},
    {"notes": [Note.C5], "duration": 0.3},
    {"notes": [Note.G4], "duration": 0.3},
    {"notes": [Note.E4], "duration": 0.3},
    # Soft, flowing bass line to complement the atmosphere
    {"notes": [Note.C3], "duration": 0.4},
    {"notes": [Note.G2], "duration": 0.4},
    {"notes": [Note.F3], "duration": 0.4},
    {"notes": [Note.G2], "duration": 0.4},
    # Main melody with gentle rising phrases
    {"notes": [Note.C4, Note.E4], "duration": 0.5},
    {"notes": [Note.G4, Note.B4], "duration": 0.5},
    {"notes": [Note.A4, Note.C5], "duration": 0.5},
    {"notes": [Note.F4, Note.A4], "duration": 0.5},
    # A gentle lift in tension, evoking the sunset's glow
    {"notes": [Note.G3, Note.B3, Note.D4], "duration": 0.3},
    {"notes": [Note.A3, Note.C4, Note.E4], "duration": 0.3},
    {"notes": [Note.B3, Note.D4, Note.F4], "duration": 0.3},
    {"notes": [Note.C4, Note.E4, Note.G4], "duration": 0.3},
    # Return to the calm bass, reflecting the fading light
    {"notes": [Note.C3], "duration": 0.4},
    {"notes": [Note.G2], "duration": 0.4},
    {"notes": [Note.F3], "duration": 0.4},
    {"notes": [Note.G2], "duration": 0.4}
]

intensely_scary_sequence = [
    # Dark, unsettling intro
    {"notes": [Note.G2], "duration": 0.3},
    {"notes": [Note.C3], "duration": 0.3},
    {"notes": [Note.E3], "duration": 0.3},
    {"notes": [Note.G3], "duration": 0.3},
    {"notes": [Note.F3], "duration": 0.3},
    {"notes": [Note.D3], "duration": 0.3},
    # Slow, menacing bass line
    {"notes": [Note.G2], "duration": 0.6},
    {"notes": [Note.F2], "duration": 0.6},
    {"notes": [Note.E2], "duration": 0.6},
    {"notes": [Note.D2], "duration": 0.6},
    # Main melody with dissonance
    {"notes": [Note.G4, Note.D5], "duration": 0.4},
    {"notes": [Note.C4, Note.F4], "duration": 0.4},
    {"notes": [Note.ASharp4, Note.E4], "duration": 0.4},
    {"notes": [Note.B3, Note.G4], "duration": 0.4},
    # Rising tension with sharp intervals
    {"notes": [Note.C5, Note.GSharp4], "duration": 0.2},
    {"notes": [Note.A4, Note.DSharp5], "duration": 0.2},
    {"notes": [Note.B4, Note.F5], "duration": 0.2},
    {"notes": [Note.C5, Note.G5], "duration": 0.2},
    # Dramatic fall
    {"notes": [Note.G4, Note.E4], "duration": 0.3},
    {"notes": [Note.F4, Note.D4], "duration": 0.3},
    {"notes": [Note.E4, Note.C4], "duration": 0.3},
    {"notes": [Note.D4, Note.B3], "duration": 0.3},
    # Loop back to ominous bass
    {"notes": [Note.G2], "duration": 0.6},
    {"notes": [Note.F2], "duration": 0.6},
    {"notes": [Note.E2], "duration": 0.6},
    {"notes": [Note.D2], "duration": 0.6}
]

super_funky_sequence = [
    # Intro funky arpeggio
    {"notes": [Note.C4], "duration": 0.2},
    {"notes": [Note.F4], "duration": 0.2},
    {"notes": [Note.G4], "duration": 0.2},
    {"notes": [Note.B4], "duration": 0.2},
    {"notes": [Note.F4], "duration": 0.2},
    {"notes": [Note.C4], "duration": 0.2},
    # Funky bass line with syncopation
    {"notes": [Note.C3], "duration": 0.3},
    {"notes": [Note.G3], "duration": 0.3},
    {"notes": [Note.F3], "duration": 0.3},
    {"notes": [Note.G3], "duration": 0.3},
    {"notes": [Note.A3], "duration": 0.3},
    {"notes": [Note.D3], "duration": 0.3},
    # Main melody with funk rhythm
    {"notes": [Note.C4, Note.E4], "duration": 0.4},
    {"notes": [Note.F4, Note.A4], "duration": 0.4},
    {"notes": [Note.G4, Note.B4], "duration": 0.4},
    {"notes": [Note.A4, Note.C5], "duration": 0.4},
    # Funky syncopated tension
    {"notes": [Note.G3, Note.C4], "duration": 0.3},
    {"notes": [Note.A3, Note.F4], "duration": 0.3},
    {"notes": [Note.B3, Note.D4], "duration": 0.3},
    {"notes": [Note.C4, Note.G4], "duration": 0.3},
    {"notes": [Note.F4, Note.A4], "duration": 0.3},
    # Funky riff with fast pace
    {"notes": [Note.C4, Note.E4, Note.G4], "duration": 0.2},
    {"notes": [Note.F4, Note.A4, Note.C5], "duration": 0.2},
    {"notes": [Note.G4, Note.B4, Note.D5], "duration": 0.2},
    {"notes": [Note.A4, Note.C5, Note.F5], "duration": 0.2},
    # Bass groove with variation
    {"notes": [Note.C3], "duration": 0.3},
    {"notes": [Note.F3], "duration": 0.3},
    {"notes": [Note.G3], "duration": 0.3},
    {"notes": [Note.A3], "duration": 0.3},
    # Main melody return
    {"notes": [Note.C4, Note.E4], "duration": 0.4},
    {"notes": [Note.F4, Note.A4], "duration": 0.4},
    {"notes": [Note.G4, Note.B4], "duration": 0.4},
    {"notes": [Note.A4, Note.C5], "duration": 0.4},
    # Rising tension with funky feel
    {"notes": [Note.G3, Note.B3, Note.D4], "duration": 0.3},
    {"notes": [Note.A3, Note.C4, Note.E4], "duration": 0.3},
    {"notes": [Note.B3, Note.D4, Note.F4], "duration": 0.3},
    {"notes": [Note.C4, Note.E4, Note.G4], "duration": 0.3},
    # Loop back to bass
    {"notes": [Note.C3], "duration": 0.3},
    {"notes": [Note.G3], "duration": 0.3},
    {"notes": [Note.F3], "duration": 0.3},
    {"notes": [Note.G3], "duration": 0.3},
    {"notes": [Note.A3], "duration": 0.3},
    {"notes": [Note.D3], "duration": 0.3}
]

cyber_punk_sequence = [
    # Intro arpeggio
    {"notes": [Note.C4], "duration": 0.2},
    {"notes": [Note.E4], "duration": 0.2},
    {"notes": [Note.G4], "duration": 0.2},
    {"notes": [Note.C5], "duration": 0.2},
    {"notes": [Note.G4], "duration": 0.2},
    {"notes": [Note.E4], "duration": 0.2},
    # Quick repeating bass line
    {"notes": [Note.C3], "duration": 0.3},
    {"notes": [Note.G2], "duration": 0.3},
    {"notes": [Note.F3], "duration": 0.3},
    {"notes": [Note.G2], "duration": 0.3},
    # Main melody
    {"notes": [Note.C4, Note.E4], "duration": 0.4},
    {"notes": [Note.G4, Note.B4], "duration": 0.4},
    {"notes": [Note.A4, Note.C5], "duration": 0.4},
    {"notes": [Note.F4, Note.A4], "duration": 0.4},
    # Rising tension
    {"notes": [Note.G3, Note.B3, Note.D4], "duration": 0.2},
    {"notes": [Note.A3, Note.C4, Note.E4], "duration": 0.2},
    {"notes": [Note.B3, Note.D4, Note.F4], "duration": 0.2},
    {"notes": [Note.C4, Note.E4, Note.G4], "duration": 0.2},
    # Loop back to bass
    {"notes": [Note.C3], "duration": 0.3},
    {"notes": [Note.G2], "duration": 0.3},
    {"notes": [Note.F3], "duration": 0.3},
    {"notes": [Note.G2], "duration": 0.3}
]


green_pastures_sequence = [
    {"notes": [Note.C4, Note.E4], "duration": 2.0},
    {"notes": [Note.G4], "duration": 2.0},
    {"notes": [Note.C5, Note.G4], "duration": 2.0},
    {"notes": [Note.F4, Note.A4], "duration": 2.0},
    {"notes": [Note.E4], "duration": 2.0},
    {"notes": [Note.D4, Note.B3], "duration": 2.0},
    {"notes": [Note.C4], "duration": 1.0},
    {"notes": [Note.A4], "duration": 1.0},
    {"notes": [Note.D4, Note.F4], "duration": 2.0},
    {"notes": [Note.G4], "duration": 2.0},
    {"notes": [Note.C5], "duration": 2.0},
    {"notes": [Note.F4, Note.A4], "duration": 2.0},
    {"notes": [Note.C4], "duration": 1.0},
    {"notes": [Note.E4], "duration": 1.0},
    {"notes": [Note.G4], "duration": 2.0},
    {"notes": [Note.D4], "duration": 1.0},
    {"notes": [Note.C5, Note.A4], "duration": 2.0},
    {"notes": [Note.F4], "duration": 2.0},
    {"notes": [Note.C4], "duration": 2.0},
    {"notes": [Note.E4], "duration": 2.0}
]


power_rangers_sequence = [
    {"notes": [Note.C4, Note.E4, Note.G4], "duration": 0.4},
    {"notes": [Note.G4, Note.A4, Note.B4], "duration": 0.4},
    {"notes": [Note.C5, Note.E5, Note.G5], "duration": 0.6},
    {"notes": [Note.A4, Note.C5, Note.E5], "duration": 0.4},
    {"notes": [Note.D5, Note.F5, Note.A5], "duration": 0.4},
    {"notes": [Note.C5, Note.E5, Note.G5], "duration": 0.4},
    {"notes": [Note.G4, Note.B4, Note.D5], "duration": 0.4},
    {"notes": [Note.A4, Note.C5, Note.E5], "duration": 0.6},
    {"notes": [Note.F5, Note.A5, Note.C6], "duration": 0.4},
    {"notes": [Note.G4, Note.B4, Note.D5], "duration": 0.4},
    {"notes": [Note.C5, Note.E5, Note.G5], "duration": 0.6},
    {"notes": [Note.D5, Note.F5, Note.A5], "duration": 0.4},
    {"notes": [Note.A4, Note.C5, Note.E5], "duration": 0.4},
    {"notes": [Note.G4, Note.B4, Note.D5], "duration": 0.6},
    {"notes": [Note.C5, Note.E5, Note.G5], "duration": 0.4}
]


keys_sequence = [
    {"notes": [Note.C4], "duration": 0.1},
    {"notes": [Note.D4], "duration": 0.1},
    {"notes": [Note.E4], "duration": 0.1},
]


# Usage example
if __name__ == "__main__":
    load_dotenv()

    # Initialize the sound engine and composer
    engine = SoundEngine()
    composer = MusicComposer(engine)

    # Play the sequence using MusicComposer
    #composer.play_sequence(retro_sequence)
    #composer.play_sequence(murky_dungeon)
    #composer.play_sequence(the_sunset_sequence)
    #composer.play_sequence(intensely_scary_sequence)
    #composer.play_sequence(super_funky_sequence)
    #composer.play_sequence(cyber_punk_sequence)
    #composer.play_sequence(green_pastures_sequence)
    #composer.play_sequence(power_rangers_sequence)
    composer.play_sequence(keys_sequence)

    # End note, stops pop-crack
    engine.play_frequency(30.0, 0.3)
    engine.play_frequency(25.0, 0.2)
    engine.play_frequency(20.0, 0.5)
