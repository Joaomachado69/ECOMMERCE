from celery import shared_task
from .models import Product, CustomerReview

@shared_task
def recalcula_avaliacao_media_produto(produto_id):
    produto = Product.objects.get(id=produto_id)
    reviews = CustomerReview.objects.filter(product=produto)
    total_reviews = len(reviews)
    if total_reviews > 0:
        soma_avaliacoes = sum(review.rating for review in reviews)
        media_avaliacoes = soma_avaliacoes / total_reviews
        produto.media_avaliacao = media_avaliacoes
        produto.save()
