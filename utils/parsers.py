from domain.Metadata import Tag

def parse_tags_from_str(tags: str) -> list[Tag]:
  result = []
  for t in tags.split(","):
    clean = t.strip().lower()
    matched = next((tag for tag in Tag if tag.value == clean), None)
    result.append(matched or Tag.UNTAGGED)
  return result