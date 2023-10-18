function toggleRule(ruleNumber) {
    var content = document.getElementById("rule-content-" + ruleNumber);
    if (content.style.display === "none" || content.style.display === "") {
        content.style.display = "block";
    } else {
        content.style.display = "none";
    }
}

const years = document.querySelectorAll(".year");

  years.forEach(year => {
      year.addEventListener("click", () => {
          years.forEach(otherYear => {
              if (otherYear !== year) {
                  otherYear.classList.remove("active");
                  otherYear.querySelector(".event-info").style.display = "none";
              }
          });

          if (!year.classList.contains("active")) {
              year.classList.add("active");
              year.querySelector(".event-info").style.display = "block";
          } else {
              year.classList.remove("active");
              year.querySelector(".event-info").style.display = "none";
          }
      });
  });