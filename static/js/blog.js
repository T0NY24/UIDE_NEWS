const form = document.getElementById("news-form");
const currentUrl = new URL(window.location.href);

form.addEventListener("submit", (event) => {
  event.preventDefault();

  const title = event.target.title.value;
  const author = event.target.author.value;
  const content = event.target.content.value;
  const category = event.target.category.value;
  const image = event.target.image.files[0];

  const formData = new FormData();
  formData.append("image", image);

  fetch("/upload-image", {
    method: "POST",
    body: formData,
  })
    .then((response) => response.json())
    .then((data) => {
      const imageUrl = data.url;

      const newsData = new FormData();

      newsData.append("title", title);
      newsData.append("author", author);
      newsData.append("content", content);
      newsData.append("category", category);
      newsData.append("imageUrl", imageUrl);

      fetch(currentUrl, {
        method: "POST",
        body: newsData,
      }).then((response) => response.json());
    });
});
