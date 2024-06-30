document.querySelectorAll(".bug").forEach(bug => {
    bug.addEventListener("click", event => {
        const dataId = event.currentTarget.getAttribute("data-id");
        const url = "/gspy/bugreports/" + dataId;
        window.location.href = url;
    })
})