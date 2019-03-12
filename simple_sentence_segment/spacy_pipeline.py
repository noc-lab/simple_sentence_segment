from simple_sentence_segment import sentence_segment


class SentenceSegmenter(object):
    def __init__(self):
        pass

    def set_sent_starts(self, doc):
        for d in doc:
            d.is_sent_start = False
        for s, _ in sentence_segment(str(doc)):
            for token in doc:
                if token.idx <= s < token.idx + len(token):
                    token.is_sent_start = True
        return doc
