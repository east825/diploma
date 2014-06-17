def suggest_classes(self, accessed_attrs):
    def unite(sets):
        return functools.reduce(set.union, sets, set())

    index = self.indexes['CLASS_ATTRIBUTE_INDEX']
    candidates = unite(index[attr] for attr in accessed_attrs)

    self.statistics['max_candidates'].set_max(len(candidates), list(accessed_attrs))

    suitable = set()
    checked = set()
    while candidates:
        candidate = candidates.pop()
        checked.add(candidate)
        bases = self._resolve_bases(candidate)

        available_attrs = unite(b.attributes for b in bases) | candidate.attributes
        if accessed_attrs <= available_attrs:
            suitable.add(candidate)

        if not self.config['FOLLOW_IMPORTS']:
            for base in bases:
                if base in checked:
                    continue
                if any(attr in base.attributes for attr in accessed_attrs):
                    candidates.add(base)

    for cls in suitable.copy():
        if any(base in suitable for base in self._resolve_bases(cls)):
            suitable.remove(cls)

    return suitable

