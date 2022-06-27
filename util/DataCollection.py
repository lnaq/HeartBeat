class DataCollection:

    def __init__(self, data: str = None) -> None:
        self.data = data

    @classmethod
    def from_csv_file(cls, file) -> str:
        print('Ret')
        return cls(data=file)

    @classmethod
    def from_excel_file(cls, file) -> str:
        return cls(data=file)

    @classmethod
    def from_txt_file(cls, file) -> str:
        data = open(file,'r').read()
        lines = data.split('\n')
        y_axis = []

        for line in lines:
            y_axis.append(line)

        return cls(data=y_axis)

    def chunker(self, seq, size: int) -> list:
        return (seq[pos:pos + size] for pos in range(0, len(seq), size))

    def remove_dublicates(self, size: int) -> list:
        free_dublicates_list = []

        for chunk in self.chunker(self.data, size):
            free_dublicates_list = free_dublicates_list + list(set(chunk))

        return free_dublicates_list
