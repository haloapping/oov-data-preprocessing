from tqdm import tqdm

class OOVNgrams:
    def create_ngrams(self, docs, context_size):
        oov_docs = []

        for doc in tqdm(docs):
            # get all idx oov token
            oov_idxs = [idx for idx, token in enumerate(doc) if token[1] is True]
            
            # All token in doc is not OOV
            if len(oov_idxs) == 0:
                continue

            # All token in doc is OOV
            elif len(oov_idxs) == len(doc):
                for oov_idx in oov_idxs:
                    oov_docs.append([doc[oov_idx]])
            else:
                for oov_idx in oov_idxs:
                    # OOV in the beginning
                    if oov_idx == 0:
                        oov_doc = []

                        if doc[oov_idx + 1][1] is True:
                            oov_doc.append(doc[oov_idx])
                        else:
                            for idx in range(len(doc) if len(doc) <= context_size else context_size + 1):
                                if idx == 0 or doc[idx][1] is False:
                                    oov_doc.append(doc[idx])
                        oov_docs.append(oov_doc)
                    
                    # OOV in the beginning
                    elif oov_idx == len(doc) - 1:
                        oov_doc = []

                        if doc[oov_idx - 1][1] is True:
                            oov_doc.append(doc[oov_idx])
                        else:
                            for idx in range(0 if len(doc) <= context_size else oov_idx - context_size, oov_idx + 1):
                                if idx == len(doc) - 1 or doc[idx][1] is False:
                                    oov_doc.append(doc[idx])
                        oov_docs.append(oov_doc)
                    
                    ## OOV in the middle
                    else:
                        left_idx = oov_idx - 1
                        left_context = []
                        left_context_size_limit = 0
                        
                        while left_idx >= 0 and doc[left_idx][1] is False:
                            if left_context_size_limit == context_size:
                                break

                            left_context.insert(0, doc[left_idx])
                            left_idx -= 1
                            left_context_size_limit += 1

                        right_idx = oov_idx + 1
                        right_context = []
                        right_context_size_limit = 0
                        
                        while right_idx < len(doc) and doc[right_idx][1] is False:
                            if right_context_size_limit == context_size:
                                break

                            right_context.append(doc[right_idx])
                            right_idx += 1
                            right_context_size_limit += 1
                                                
                        oov_docs.append(left_context + [doc[oov_idx]] + right_context)

        return oov_docs
            

    def split_ngrams(self, ngrams, lowercase_oov=True):
        contexts = []

        for ngram in tqdm(ngrams):
            oov_idx = [idx for idx, token in enumerate(ngram) if token[1] is True][0]
            contexts.append(
                ([token[0] for token in ngram[:oov_idx]],
                list(ngram[oov_idx][0].lower()) if lowercase_oov else list(ngram[oov_idx][0]),
                [token[0] for token in ngram[oov_idx + 1:]]
            ))

        return contexts

    def left_context(self, ngrams):
        ngrams_docs = self.split_ngrams(ngrams)

        return [doc[0] for doc in ngrams_docs]
    
    def right_context(self, ngrams):
        ngrams_docs = self.split_ngrams(ngrams)

        return [doc[-1] for doc in ngrams_docs]

    def oov_context(self, ngrams):
        ngrams_docs = self.split_ngrams(ngrams)

        return [doc[1] for doc in ngrams_docs]
        