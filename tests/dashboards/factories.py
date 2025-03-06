import factory
from django.utils.text import slugify

from pilotage.dashboards.models import Category, Dashboard


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category
        skip_postgeneration_save = True

    title = factory.Faker("words")


class DashboardFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Dashboard
        skip_postgeneration_save = True

    class Params:
        for_snapshot = factory.Trait(
            title="super duper title",
            baseline="super duper baseline",
            description="super duper description",
            metabase_db_id=0,
            tally_embed_id="5up3rdup3r",
        )

    title = factory.Faker("words")
    baseline = factory.Faker("sentence")
    slug = factory.LazyAttribute(lambda obj: slugify(obj.title))
    category = factory.SubFactory(CategoryFactory)
    metabase_db_id = factory.Faker("pyint")
    description = factory.Faker("text")
    tally_popup_id = factory.Faker("pystr", prefix="popup", max_chars=5)
    tally_embed_id = factory.Faker("pystr", prefix="embed", max_chars=5)
