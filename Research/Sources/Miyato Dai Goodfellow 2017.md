# Adversarial Training Methods for Semi-Supervised Text Classification

## Bibliography

- **Authors:** Takeru Miyato, Andrew M. Dai, Ian Goodfellow
- **Date / version:** arXiv:1605.07725, first submitted May 2016; revised 2021; published at ICLR 2017.
- **Primary link:** [arXiv:1605.07725](https://arxiv.org/abs/1605.07725)
- **PDF / HTML:** [PDF](https://arxiv.org/pdf/1605.07725) · [HTML](https://arxiv.org/html/1605.07725v4)
- **Code:** linked from the paper to the TensorFlow Models repository.

## Assessment

- **Evidence grade:** 2 — peer-reviewed ML methodology paper, but domain is text classification, not financial return prediction.
- **Recency:** 2017 publication/revised 2021; methods remain educational, while current alternatives should be compared.
- **Novelty:** Demonstrates embedding-space adversarial perturbations for regularization in semi-supervised sequence models.
- **Source type:** Conference paper / arXiv.

## Summary

The authors adapt adversarial and virtual adversarial training to sparse text inputs by perturbing learned word embeddings in recurrent neural networks. They report benchmark improvements and reduced overfitting in their target tasks.

## Research use and limitations

This is a useful example of regularization and sequence modeling, not evidence that an adversarially trained LSTM predicts tradable returns. For market applications, define the perturbation meaning, validate chronologically, account for nonstationarity and costs, and test against simple baselines.

## Connected notes

[[Deep learning]] · [[Sequence models]] · [[Overfitting controls]] · [[ML validation]]
