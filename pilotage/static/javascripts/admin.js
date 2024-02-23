let textareas = document.querySelectorAll("textarea");

if (textareas.length) {
  const easyMDE = new EasyMDE({
    toolbar: [
      {
        name: "heading",
        action: EasyMDE.toggleHeadingSmaller,
        className: "fa fa-header",
        title: "Headers",
        children: [
          {
            name: "heading-2",
            action: EasyMDE.toggleHeading2,
            className: "fa fa-header header-2",
            title: "Medium Heading",
          },
          {
            name: "heading-3",
            action: EasyMDE.toggleHeading3,
            className: "fa fa-header header-3",
            title: "Small Heading",
          },
        ],
      },
      "bold",
      "italic",
      "unordered-list",
      "link",
    ],
    spellChecker: false,
  });
}

