def parse_secons_to_text(time: int) -> str:
  seconds = time % 60
  minutes = round(time / 60 % 60)
  hours = round(time / 60**2 % 60**2)
  days = round(time / (60**2 * 24) % (60**2 * 24)) 
  weeks = round(time / (60**2 * 24 * 7))

  #TODO: fix plural
  return (
    f"The link will expire in: "
    f"{str(weeks) + ' weeks ' if weeks > 0 else ''}"
    f"{str(days) + ' days ' if days > 0 else ''}"
    f"{str(hours) + ' hours ' if hours > 0 else ''}"
    f"{str(minutes) + ' minutes ' if minutes > 0 else ''}"
    f"{str(seconds) + ' seconds ' if seconds > 0 else ''}"
  )
