from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import List


class Tag(Enum):
  FRIENDLY = "friendly"
  OFFENSIVE = "offensive"
  SILLY = "silly"
  WAREDIT = "waredit"
  UNTAGGED = "untagged"


@dataclass
class Metadata:
  key: str = ""
  created_at: datetime = field(default_factory=datetime.now(timezone.utc))
  updated_at: datetime = field(default_factory=datetime.now(timezone.utc))
  tags: List[Tag] = field(default_factory=list)

  @staticmethod
  def from_dict(data: dict):
    return Metadata(
      key=data.get("key"),
      created_at=data.get("created_at", datetime.now(timezone.utc)),
      updated_at=data.get("updated_at", datetime.now(timezone.utc)),
      tags=data.get("tags", []),
    )

  def to_dict(self):
    return {
      "key": self.key,
      "created_at": self.created_at,
      "updated_at": self.updated_at,
      "tags": self.tags,
    }

  def update_url(self, new_url: str):
    self.url = new_url
    self.updated_at = datetime.now(timezone.utc)

  def add_tag(self, tag: Tag):
    if tag not in self.tags:
      self.tags.append(tag)
      self.updated_at = datetime.now(timezone.utc)

  def remove_tag(self, tag: Tag):
    if tag in self.tags:
      self.tags.remove(tag)
      self.updated_at = datetime.now(timezone.utc)


# Update these classes in future. For now only Video content is present
# @dataclass
# class Photo(Metadata):
  

# @dataclass
# class Video(Metadata):
  
