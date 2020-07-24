// Function to make sure document is loaded and ready for javascript execution
function documentReady(fn) {
    // see if DOM is already available
    if (document.readyState === "complete" || document.readyState === "interactive") {
        // call on next available tick
        setTimeout(fn, 1);
    }
    else {
        document.addEventListener("DOMContentLoaded", fn);
    }
} 
// Run script when document ready
documentReady(function() {
    // DOM is loaded and ready for manipulation here
    // alert("Hello Ireland!");
});

// Google Maps API Key: AIzaSyCteoDnjGZSN2Jze1xindy4jo3sy_sHcp4