import pytest
from core.models import Post
from core.models import User
from core.schemas import QuotePostInSchema
from core.services import create_quote_post
from model_bakery import baker


@pytest.mark.django_db
def test_create(user, faker):
    post = baker.make(Post)
    payload = QuotePostInSchema(post_id=post.id, comment=faker.text())

    create_quote_post(user.id, payload)

    assert Post.objects.count() == 2


@pytest.mark.django_db
def test_save_correctly(user, faker):
    other_user = baker.make(User)
    post = baker.make(Post, user=other_user)
    comment = faker.text()
    payload = QuotePostInSchema(post_id=post.id, comment=comment)

    create_quote_post(user.id, payload)

    quote_post = Post.objects.last()
    assert quote_post.user.id == user.id
    assert quote_post.comment == comment
    assert quote_post.content == post.content
    assert quote_post.type == Post.Type.QUOTE


@pytest.mark.django_db
def test_return(user, faker):
    post = baker.make(Post)
    payload = QuotePostInSchema(post_id=post.id, comment=faker.text())

    quote_post = create_quote_post(user.id, payload)

    assert isinstance(quote_post, Post)
