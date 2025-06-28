from sklearn.metrics.pairwise import cosine_similarity

def compute_similarity(resume_vec, job_vecs):
    return cosine_similarity(resume_vec, job_vecs).flatten()