import json
import os
from typing import Optional, List


class Template:
    def __init__(self, name: str, templates_file: str = "templates.json"):
        self.name = name
        self.templates_file = templates_file
        self.subject = ""
        self.body = ""
        self.subject = ""
        self.body = ""
        self.attachments = []

        self.load_templates()

    def load_templates(self):
        with open(self.templates_file, "r") as file:
            templates = json.load(file)

        template = templates.get(self.name)
        if not template:
            raise ValueError(f"Unknown template name: {self.name}")

        self.subject = template["subject"]
        body_path = template["body_path"]
        self.body = self.load_body(body_path)
        self.attachments = template.get("attachments", [])

    def load_body(self, body_path: str) -> str:
        _, file_extension = os.path.splitext(body_path)
        with open(body_path, "r") as file:
            if file_extension in [".html", ".md", ".txt"]:
                return file.read()
            else:
                raise ValueError(f"Unsupported file type: {file_extension}")

    def set(self, **kwargs):
        self.subject = self.subject.format(**kwargs)
        self.body = self.body.format(**kwargs)

    def set_attachments(self, attachments: Optional[List[str]] = None):
        if attachments:
            self.attachments.extend(attachments)

    def __iter__(self):
        yield "subject", self.subject
        yield "body", self.body
        yield "attachments", self.attachments
