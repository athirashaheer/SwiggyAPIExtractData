param (
    [Parameter(Mandatory = $true)]
    [string]$restaurantId
)

# Define the API URL
$url = "https://www.swiggy.com/dapi/menu/pl?page-type=REGULAR_MENU&complete-menu=true&lat=18.56&lng=73.95&restaurantId=$restaurantId"

try
{
    # Send a GET request to the API URL
    $response = Invoke-WebRequest -Uri $url -ErrorAction Stop

    # Convert the content from JSON to a PowerShell object
    $menuData = $response.Content | ConvertFrom-Json

    # Extract the menu items
    $menuList = $menuData.data.cards.groupedCard.cardGroupMap.REGULAR.Cards.card.card.itemcards.card.info | Select-Object name, category, description

    # Export the menu items to a CSV file
    $menuList | Export-Csv -Path ".\menu_data_$restaurantId.csv" -NoTypeInformation
}
catch
{
    Write-Host "An error occurred: $_"
}
