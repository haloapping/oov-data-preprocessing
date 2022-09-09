from copy import deepcopy


class Util:
    def padding(self, docs, mode="post", padding_val="</PAD>"):
        docs = deepcopy(docs)
        max_doc_len = max(len(doc) for doc in docs)
        pad_docs = []

        for doc in docs:
            for _ in range(max_doc_len - len(doc)):
                if mode == "post":
                    doc.append(padding_val)
                elif mode == "pre":
                    doc.insert(0, padding_val)
                else:
                    raise ValueError(f"mode = {mode} is not available, use instead 'pre' or 'post'.")
            pad_docs.append(doc)

        return pad_docs

    def vocabs(self, tokens):
        return list(set(tokens))

    def token_to_idx(self, vocabs):
        return {vocab : idx for idx, vocab in enumerate(vocabs)}

    def idx_to_token(self, vocabs):
        return {idx : vocab for idx, vocab in enumerate(vocabs)}