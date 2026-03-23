from processor import AudioProcessor


def main():
    pass

if __name__ == "__main__":
    proc = AudioProcessor()
    while True:
        raw_data = proc.read_chunk()
        print(raw_data[0:10])

