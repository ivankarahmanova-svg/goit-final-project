class Note:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content
        self.tags: list[str] = []

    def add_tag(self, tag: str) -> None:
        if tag not in self.tags:
            self.tags.append(tag)

    def remove_tag(self, tag: str) -> None:
        if tag in self.tags:
            self.tags.remove(tag)

    def edit_content(self, new_content: str) -> None:
        self.content = new_content

    def __str__(self) -> str:
        tags_str = ", ".join(self.tags) if self.tags else "no tags"
        return f"Title: {self.title}, Content: {self.content}, Tags: {tags_str}"


class NotesBook:
    def __init__(self) -> None:
        self.notes: list[Note] = []

    def add_note(self, note: Note) -> None:
        self.notes.append(note)

    def find_by_title(self, title: str) -> Note | None:
        for note in self.notes:
            if note.title.lower() == title.lower():
                return note
        return None

    def find_by_tag(self, tag: str) -> list[Note]:
        return [note for note in self.notes if tag in note.tags]

    def delete_note(self, title: str) -> bool:
        note = self.find_by_title(title)
        if note is not None:
            self.notes.remove(note)
            return True
        return False

    def show_all(self) -> str:
        if not self.notes:
            return "No notes saved."
        return "\n".join(str(note) for note in self.notes)
    def sort_by_tags(self):
        return sorted(self.notes, key=lambda note: ", ".join(note.tags))