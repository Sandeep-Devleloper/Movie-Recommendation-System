
let recom = document.getElementById('recommendations');

document.getElementById('submit').addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent form submission
    scrollToRecommendations(); // Call the scroll function
});
document.getElementById('yes-btn').addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent form submission
    scrollToRecommendations(); // Call the scroll function
});


function scrollToRecommendations() {
    recom.scrollTop = recom.scrollHeight; // Scroll to the bottom
}


document.getElementById('copy-btn').addEventListener('click', function () {
    // Get the ordered list
    const list = document.getElementById('recommendations');

    // Create a range and select the list
    const range = document.createRange();
    range.selectNode(list);

    // Clear any current selections
    window.getSelection().removeAllRanges();
    window.getSelection().addRange(range);

    // Copy the selection to clipboard
    try {
        document.execCommand('copy');
        alert('List copied to clipboard!');
    } catch (err) {
        console.error('Could not copy text: ', err);
    }

    // Clear selection
    window.getSelection().removeAllRanges();
});