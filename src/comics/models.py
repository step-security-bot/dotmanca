from django.db import models
from django.urls import reverse


def arc_image_upload_to(instance, file_name):
    file_extension = file_name.split(".")[-1]
    return f"galleries/{instance.slug}.{file_extension}"


class Arc(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    sort_order = models.IntegerField()
    the_image = models.ImageField(
        null=False,
        blank=False,
        upload_to=arc_image_upload_to,
    )

    def __str__(self):
        return f"{self.name} (Arc)"

    class Meta:
        ordering = ("sort_order",)


def issue_image_upload_to(instance, file_name):
    file_extension = file_name.split(".")[-1]
    return f"galleries/{instance.arc.slug}/{instance.slug}.{file_extension}"


class Issue(models.Model):
    arc = models.ForeignKey(Arc, on_delete=models.CASCADE, related_name="issues")
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    description = models.TextField(blank=True)
    sort_order = models.IntegerField()
    the_image = models.ImageField(
        null=False,
        blank=False,
        upload_to=arc_image_upload_to,
    )

    gallery = models.OneToOneField(
        "gallery.Gallery", on_delete=models.CASCADE, null=True, blank=True
    )

    def get_absolute_url(self):
        kwargs = {"slug": self.slug, "arc_slug": self.arc.slug}
        return reverse("comics:issue", kwargs=kwargs)

    def __str__(self):
        return f"{self.name} ({self.arc.name})"

    class Meta:
        ordering = ("sort_order",)
        unique_together = ("arc", "slug")
