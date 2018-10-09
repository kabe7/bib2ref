<$publications>
<$pubType=article?>
(<$authors.firstName.stringByRemovingTeX.@componentsWithEtAlAfterOne/> <$fields.Year/>) [<$fields.Title/>](<$remoteURLs.URL.@firstObject/>), _<$fields.Journal/>_, <$fields.Volume/><$fields.Number.parenthesizedStringIfNotEmpty/>: <$fields.Pages/>.

<?$pubType=inproceedings?>
(<$authors.firstName.stringByRemovingTeX.@componentsWithEtAlAfterOne/> <$fields.Year/>) [<$fields.Title/>](<$remoteURLs.URL.@firstObject/>), _<$fields.Series/> <$fields.Year/>_, pp.<$fields.Pages/>.

<?$pubType=incollection?>
(<$authors.firstName.stringByRemovingTeX.@componentsWithEtAlAfterOne/> <$fields.Year/>) [<$fields.Title/>](<$remoteURLs.URL.@firstObject/>), _<$fields.Booktitle/>_, pp.<$fields.Pages/>.

<?$pubType?>
(<$authors.firstName.stringByRemovingTeX.@componentsWithEtAlAfterOne/> <$fields.Year/>) [<$fields.Title/>](<$remoteURLs.URL.@firstObject/>)

</$pubType?>
</$publications>

