"""Tiny BM25 search. No dependencies, no paid service."""
import math, re
from collections import Counter

STOP = set("a an the and or of to in on for is are was were be it this that with as at by from".split())

def tokenize(text):
    return [t for t in re.findall(r"[a-z0-9']+", text.lower()) if t not in STOP]

class BM25:
    def __init__(self, chunks, k1=1.5, b=0.75):
        self.chunks = chunks
        self.k1, self.b = k1, b
        self.tokens = [tokenize(c["text"]) for c in chunks]
        self.tf = [Counter(t) for t in self.tokens]
        self.avg = (sum(len(t) for t in self.tokens) / len(self.tokens)) if self.tokens else 0
        df = Counter()
        for t in self.tokens:
            df.update(set(t))
        n = len(self.tokens)
        self.idf = {w: math.log(1 + (n - d + 0.5) / (d + 0.5)) for w, d in df.items()}

    def search(self, query, k=4):
        q = tokenize(query)
        scored = []
        for i, tf in enumerate(self.tf):
            dl = len(self.tokens[i]) or 1
            s = 0.0
            for w in q:
                if w not in tf:
                    continue
                f = tf[w]
                s += self.idf.get(w, 0) * f * (self.k1 + 1) / (f + self.k1 * (1 - self.b + self.b * dl / self.avg))
            if s > 0:
                scored.append((s, i))
        scored.sort(reverse=True)
        return [dict(self.chunks[i], score=round(s, 3)) for s, i in scored[:k]]
