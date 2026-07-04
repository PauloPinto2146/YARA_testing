browser.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {

    if (changeInfo.status !== "complete")
        return;

    console.log(`VISITOU: ${tab.title} (${tab.url})`);
});