from typing import List
from synth.sound_engine import SoundEngine


class MusicComposer:
    def __init__(self, engine: SoundEngine):
        """
        Initializes the music composer with a sound engine.
        :param engine: Instance of SoundEngine to use for playback and file writing.
        """
        self.engine = engine

    def play_sequence(self, sequence: List[dict]):
        """
        Plays a sequence of notes or chords.
        :param sequence: List of dictionaries specifying notes, duration, and optional filename.
        Example:
        [
            {"notes": ["C3", "E3", "G3"], "duration": 3.0},
            {"notes": [440.0, 550.0, 660.0], "duration": 2.0, "save_to": "chord.wav"}
        ]
        """
        for item in sequence:
            notes = item["notes"]
            duration = item["duration"]
            filename = item.get("save_to")

            if filename:
                self.engine.save_wave(notes, duration, filename)
            else:
                self.engine.play_chord(notes, duration)
