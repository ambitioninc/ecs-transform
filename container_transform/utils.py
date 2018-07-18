def flatten(lst, final=None):
  if final is None:
    final = []

  for val in lst:
    if isinstance(val, list):
      flatten(val, final)
    else:
      final.append(val)

  return final
