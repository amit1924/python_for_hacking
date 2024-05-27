document.addEventListener("DOMContentLoaded", () => {
  const nameSearch = document.getElementById("search");
  const projects = document.querySelectorAll(".project");
  const tags = document.querySelectorAll(".tag");

  function filterProjects() {
    const nameQuery = nameSearch.value.toLowerCase();
    projects.forEach((project) => {
      const name = project.getAttribute("data-name");
      const nameMatch = name.includes(nameQuery);
      if (nameMatch) {
        project.style.display = "";
      } else {
        project.style.display = "none";
      }
    });
  }

  tags.forEach((tag) => {
    tag.addEventListener("click", () => {
      const selectedTag = tag.getAttribute("data-tag");
      projects.forEach((project) => {
        const projectTags = project.getAttribute("data-tags");
        if (projectTags.includes(selectedTag)) {
          project.style.display = "";
        } else {
          project.style.display = "none";
        }
      });
    });
  });

  nameSearch.addEventListener("keyup", filterProjects);
});
