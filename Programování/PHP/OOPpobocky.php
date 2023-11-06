<?php

class Pracovni_Pozice {
    private static array $list = [];

    public function __construct(private string $nazev) {
        self::$list[] = $this;
    }

    /**
     * @return string
     */
    public function getNazev(): string
    {
        return $this->nazev;
    }

    /**
     * @return array
     */
    public static function seznamPozic(): array
    {
        return self::$list;
    }
}

class Zamestnanec {
    private static array $list = [];

    public function __construct(private string $jmeno, private string $prijmeni, private int $id, private Pracovni_Pozice $pozice)
    {
        self::$list[] = $this;
    }

    /**
     * @return string
     */
    public function getJmeno(): string
    {
        return $this->jmeno;
    }

    /**
     * @return string
     */
    public function getPrijmeni(): string
    {
        return $this->prijmeni;
    }

    /**
     * @return int
     */
    public function getId(): int
    {
        return $this->id;
    }

    /**
     * @return Pracovni_Pozice
     */
    public function getPozice(): Pracovni_Pozice
    {
        return $this->pozice;
    }

    /**
     * @return array
     */
    public static function seznamZamestnancu(): array
    {
        return self::$list;
    }
}

class Pobocka {
    /**
     * @var array|Pobocka[]
     */
    private static array $list = [];
    /**
     * @var array|Zamestnanec[]
     */
    private array $zamestanci = [];

    public function __construct(private string $nazev, private string $psc, private string $mesto, private int $cislo_popisne)
    {
        self::$list[] = $this;
    }

    public function addZamestnanec(Zamestnanec $zamestnanec): void {
        $this->zamestanci[] = $zamestnanec;
    }

    /**
     * @return array|Zamestnanec[]
     */
    public function seznamZamestnancu(): array {
        return $this->zamestanci;
    }

    /**
     * @return string
     */
    public function getMesto(): string
    {
        return $this->mesto;
    }

    /**
     * @return string
     */
    public function getNazev(): string
    {
        return $this->nazev;
    }

    /**
     * @return int
     */
    public function getCisloPopisne(): int
    {
        return $this->cislo_popisne;
    }

    /**
     * @return string
     */
    public function getPsc(): string
    {
        return $this->psc;
    }

    /**
     * @return array|Pobocka[]
     */
    public static function seznamPobocek(): array
    {
        return self::$list;
    }
}

$vedouci = new Pracovni_Pozice("Vedoucí podniku");
$delnik = new Pracovni_Pozice("Dělník");
$makler = new Pracovni_Pozice("Makléř");

echo "Počet pracovních pozic celkově: " . count(Pracovni_Pozice::seznamPozic()) . "\n";


$pepa = new Zamestnanec("Pepa", "Fotr", 47, $vedouci);
$radim = new Zamestnanec("Radim", "Lotr", 49985, $vedouci);
$adam = new Zamestnanec("Adam", "Lotr", 49985, $delnik);
$matej = new Zamestnanec("Matej", "Kostrč", 5,$makler);

echo "Počet zaměstanců celkově: " . count(Zamestnanec::seznamZamestnancu()) . "\n";

$marianska = new Pobocka("Mariánská", "407 47", "Varnsdorf", 320);
$marianska->addZamestnanec($pepa);
$marianska->addZamestnanec($radim);
echo "Mariánská - zaměstancni: \n";
foreach ($marianska->seznamZamestnancu() as $zamestnanec) {
    echo $zamestnanec->getJmeno() . " " . $zamestnanec->getPrijmeni() . "\n";
}

$kotlarska = new Pobocka("Kotlářská", "407 47", "Varnsdorf", 325);
$kotlarska->addZamestnanec($adam);
$kotlarska->addZamestnanec($matej);
echo "\nKotlářská - zaměstancni: \n";
foreach ($kotlarska->seznamZamestnancu() as $zamestnanec) {
    echo $zamestnanec->getJmeno() . " " . $zamestnanec->getPrijmeni() . "\n";
}
