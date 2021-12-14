using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.InteropServices.WindowsRuntime;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Xml;

namespace XMLConverter
{
    class DOMXMLStrategy : IStrategyParser
    {
        public List<ProgLanguage> Parse(ProgLanguage searchParams) 
        {
            List<ProgLanguage> languages = new List<ProgLanguage>();
            XmlDocument doc = new XmlDocument();
            doc.Load(@"C:\Users\Vlad_2\repos\C#\XMLConverter\XMLConverter\ProgLanguages.xml");

            XmlNode root = doc.DocumentElement;

            foreach (XmlNode node in root.ChildNodes)
            {
                ProgLanguage languageObj = new ProgLanguage();
                foreach (XmlAttribute attribute in node.Attributes) 
                {
                    if (attribute.Name == "Authors" && (searchParams.Authors == attribute.Value || searchParams.Authors == ""))
                    {
                        languageObj.Authors = attribute.Value;
                        Console.WriteLine("Added authors");
                    }
                    if (attribute.Name == "LanguageName" && (searchParams.LanguageName == attribute.Value || searchParams.LanguageName == ""))
                    {
                        languageObj.LanguageName = attribute.Value;
                        Console.WriteLine("Added name");
                    }
                    if (attribute.Name == "ReleaseYear" && (searchParams.ReleaseYear == attribute.Value || searchParams.ReleaseYear == ""))
                    {
                        languageObj.ReleaseYear = attribute.Value;
                        Console.WriteLine("Added release year");
                    }
                    
                    if (attribute.Name == "TypeOfLanguage" && (searchParams.TypeOfLanguage == attribute.Value || searchParams.TypeOfLanguage == ""))
                    {
                        languageObj.TypeOfLanguage = attribute.Value;
                        Console.WriteLine("Added type");
                    }
                    if (attribute.Name == "AbstractionLevel" && (searchParams.AbstractionLevel == attribute.Value || searchParams.AbstractionLevel == ""))
                    {
                        languageObj.AbstractionLevel = attribute.Value;
                        Console.WriteLine("Added abs level");
                    }
                    if (attribute.Name == "CommonlyUsedFor" && (searchParams.CommonlyUsedFor == attribute.Value || searchParams.CommonlyUsedFor == ""))
                    {
                        languageObj.CommonlyUsedFor = attribute.Value;
                        Console.WriteLine("Added common usage");
                    }
                }
                if (!languageObj.HasSomeFieldsEmpty()) 
                {
                    languages.Add(languageObj);
                }
            }
            return languages;
        }
    }
}
