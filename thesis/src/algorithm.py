def suggest_classes(self, accessed_attrs):
    def unite(sets):
        return functools.reduce(set.union, sets, set())

    def intersect(sets):
        return functools.reduce(set.intersection, sets) if sets else set()

    # More fair algorithm because it considers newly discovered bases classes as well
    index = self.indexes['CLASS_ATTRIBUTE_INDEX']
    candidates = unite(index[attr] for attr in accessed_attrs)

    self.statistics['max_candidates'].set_max(len(candidates), list(accessed_attrs))

    suitable = set()
    checked = set()
    while candidates:
        candidate = candidates.pop()
        checked.add(candidate)
        bases = self._resolve_bases(candidate)

        # register number of base classes for statistics
        self.statistics['max_bases'].set_max(len(bases), candidate.qname)

        available_attrs = unite(b.attributes for b in bases) | candidate.attributes
        if accessed_attrs <= available_attrs:
            suitable.add(candidate)

        # new classes could be added to index during call to _resolve_bases(),
        # so we have to check them as well
        if not self.config['FOLLOW_IMPORTS']:
            for base in bases:
                if base in checked:
                    continue
                if any(attr in base.attributes for attr in accessed_attrs):
                    candidates.add(base)

    # remove subclasses if their superclasses is suitable also
    for cls in suitable.copy():
        if any(base in suitable for base in self._resolve_bases(cls)):
            suitable.remove(cls)

    return suitable

