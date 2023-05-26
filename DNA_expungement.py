class DNADatabase:
    def __init__(self):
        # For simplicity, we represent the DNA database as a dictionary
        # with person's name as the key and their DNA data as the value
        self.data = {}

    def add(self, name, dna_data):
        self.data[name] = dna_data
        print(f"DNA data added for {name}.")

    def expunge(self, name):
        if name in self.data:
            del self.data[name]
            print(f"DNA data expunged for {name}.")
        else:
            print(f"No DNA data found for {name}.")

# Sample usage
if __name__ == "__main__":
    dna_db = DNADatabase()

    dna_db.add("John Doe", "ACGTACGTACGT")
    dna_db.add("Jane Smith", "TGACTGACTGAC")

    dna_db.expunge("John Doe")
